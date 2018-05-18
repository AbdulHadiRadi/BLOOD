from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from notifications.signals import notify
from psycopg2._psycopg import Notify
from rest_framework.response import Response
from rest_framework.serializers import (
    CharField,
    IntegerField,
    DateField,
    EmailField,
    DateTimeField,
    BooleanField,
    DecimalField,
    ImageField,
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    Serializer)
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from social_core.pipeline import user

from .models import (
    User,
    Account,
    Donor,
    Request,
    Blood,
    Notification)

from django.core.validators import RegexValidator


class UserSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_donor')
        extra_kwargs = {"password": {"write_only": True}}

class ChangePasswordSerializer(Serializer):
    email = CharField(required=True)
    new_password = CharField(required=True)
    id = IntegerField(read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        new_password = data.get('new_password', None)

        try:
            user = User.objects.get(email=email, is_donor = True)
            if not user:
                raise ValidationError("This user account doesn't exists.")
            user.set_password(new_password)
            user.save()
            return user

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError("This user account doesn't exists.")


class UserCreateSerializer(ModelSerializer):
    id = IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_donor')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validate_data):
        user = super().create(validate_data)
        password = validate_data['password']
        user.set_password(password)
        user.save()
        return validate_data


class UserUpdateSerializer(ModelSerializer):
    email = EmailField(read_only=True)
    is_donor = BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ('email','first_name','last_name','is_donor')


class ProfileUpdateSerializer(ModelSerializer):
    email = EmailField(read_only=True)
    class Meta:
        model = User
        fields = ('first_name','last_name', 'phone_number')


class UserLoginSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    id = IntegerField(read_only=True)
    first_name = CharField(read_only=True)
    last_name = CharField(read_only=True)
    bloodGroup = SerializerMethodField(read_only=True)
    last_donated_date = SerializerMethodField(read_only=True)
    capable = SerializerMethodField(read_only=True)
    city = SerializerMethodField(read_only=True)
    country = SerializerMethodField(read_only=True)
    donID = SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name','last_name', 'bloodGroup', 'last_donated_date', 'capable', 'city', 'country', 'donID')
        extra_kwargs = {"password": {"write_only": True}}


    def get_bloodGroup(self, obj):
         u = User.objects.get(email=obj.email)
         return u.donor.bloodGroup


    def get_last_donated_date(self, obj):
         u = User.objects.get(email=obj.email)
         return u.donor.last_donated_date


    def get_capable (self, obj):
         u = User.objects.get(email=obj.email)
         return u.donor.capable

    def get_city(self, obj):
        u = User.objects.get(email=obj.email)
        return u.account.city

    def get_country(self, obj):
        u = User.objects.get(email=obj.email)
        return u.account.country

    def get_donID (self, obj):
        u = User.objects.get(email=obj.email)
        return u.donor.pk

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        try:
            user = User.objects.get(email=email, is_donor=True)
            if user:
                if not user.check_password(password):
                    raise ValidationError( "Incorrect credentials please try again.")
                return user
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError("This user account doesn't exists or inactive.")



class UserLogoutSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'email')


##Get Account ID
class AccountIDSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'user')

class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = ('city', 'country')

class DonorAccountSerializer(ModelSerializer):
    bloodGroup = CharField(source='user.donor.bloodGroup')
    capable = CharField (source='user.donor.capable')

    class Meta:
        model = Account
        fields = ( 'bloodGroup', 'capable', 'city', 'country')


#Get Donor ID
class DonorIDSerializer(ModelSerializer):
    class Meta:
        model = Donor
        fields = ('id', 'user')


class DonorSerializer(ModelSerializer):

    class Meta:
        model = Donor
        fields = ('bloodGroup', 'last_donated_date', 'capable')

class DonorUpdateSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Donor
        fields = ('user', 'bloodGroup','birth_date', 'capable')

class DonatedDateUpdateSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Donor
        fields = ('user', 'last_donated_date', 'capable')

class RequestSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    class Meta:
        model = Request
        fields = ('id', 'user','bloodGroup', 'street', 'road', 'city', 'state', 'country', 'post_code', 'time', 'bags')



class GetDonorSerializer(ModelSerializer):

    class Meta:
        model = Donor
        fields = ('user', 'bloodGroup')



class BloodCollectionSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Blood
        fields = ('user', 'o_pos', 'o_neg', 'a_pos', 'a_neg', 'b_pos', 'b_neg', 'ab_pos', 'ab_neg')


class NotificationSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    class Meta:
        model = Notification
        fields = ('id',  'interested')

class AccDonUpdate(Serializer):
    email = CharField(required=True)
    bloodGroup = CharField(required=True)
    birth_date = CharField(required=True)
    phone_number = CharField(required=True)
    street = CharField(required=True)
    road = CharField(required=True)
    city = CharField(required=True)
    state = CharField(required=True)
    country = CharField(required=True)
    post_code = CharField(required=True)

    def validate(self, data):
        email = data.get('email', None)
        bloodGroup = data.get('bloodGroup', None)
        birth_date = data.get('birth_date', None)
        phone_number = data.get('phone_number', None)
        street = data.get('street', None)
        road = data.get('road', None)
        city = data.get('city', None)
        state = data.get('state', None)
        country = data.get('country', None)
        post_code = data.get('post_code', None)

        try:
            user = User.objects.get(email=email, is_donor = True)
            if not user:
                print("not")
                raise ValidationError("This user account doesn't exists.")
            user.donor.bloodGroup = bloodGroup
            user.donor.birth_date = birth_date
            user.account.phone_number = phone_number
            user.account.street = street
            user.account.road = road
            user.account.city = city
            user.account.state = state
            user.account.country = country
            user.account.post_code =post_code
            user.donor.save()
            user.account.save()
            return user

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError("This user account doesn't exists.")