from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)
from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from api.models import User,Account, Request
from django.utils.safestring import mark_safe






BLOOD_CHOICES= [
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ]



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254, help_text= mark_safe('<strong> A valid Email is Required To Register in BDonate.</strong>'), widget=forms.TextInput(attrs={'size':72}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'size':72}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'size': 72}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'size':72}),
                                help_text='Your password can not be too similar to your other personal information and must contain at least 8 characters. It can not be a commonly used password or entirely numeric.')
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'size':72}),
                                help_text=' Enter the same password as before,for verification.')
    blood_group = forms.CharField(label='What is your blood group?', widget=forms.Select(choices=BLOOD_CHOICES))
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD', widget=forms.DateInput(attrs={'size':72}))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=15, empty_value=0, help_text="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                   widget=forms.NumberInput(attrs={'size':72}))  # validators should be a list

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'birth_date', 'blood_group', 'phone_number')



    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This Email had already registered!')
        return email

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        if birth_date > date.today():
            raise forms.ValidationError("The date cannot be in the future!")
        if ((abs(date.today() - birth_date).days) < 6205):
            raise forms.ValidationError("Minimum required Age is 17!")
        return birth_date





class HospitalSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254, widget=forms.TextInput(attrs={'size':72}),
                             help_text=mark_safe('<strong> A valid Email is Required To Register in BDonate.</strong>'))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'size':72}),
                                help_text='Your password can not be too similar to your other personal information and must contain at least 8 characters. It can not be a commonly used password or entirely numeric.')
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'size':72}),
                                help_text=' Enter the same password as before,for verification.')
    first_name = forms.CharField(label='Hospital | Blood Bank Name', widget=forms.TextInput(attrs={'size':72}), max_length=500)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=15, empty_value=0,
                                   widget=forms.NumberInput(attrs={'size': 72}),
                                   help_text="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")  # validators should be a list

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'phone_number')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This Email had already registered!')
        return email



class AddressForm(forms.Form):
    street_number = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'id':"street_number", 'size':72}))
    road = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'id':"route",'size':72}))
    city = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'id':"locality", 'size':72}))
    state = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'id':"administrative_area_level_1", 'size':72}))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'id':"country", 'size':72}))
    postal_code = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'id':"postal_code", 'size':72}))

    class Meta:
        model = Account
        fields = ('street_number', 'road', 'city', 'state', 'country', 'postal_code')

