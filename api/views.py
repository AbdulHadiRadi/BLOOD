from datetime import datetime, date, timedelta
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_403_FORBIDDEN
from rest_framework.views import APIView
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from .models import User, Account, Donor, Request, Blood, Notification
from .serializers import (
    UserUpdateSerializer,
    UserLoginSerializer,
    AccountIDSerializer,
    DonorIDSerializer,
    DonorUpdateSerializer,
    RequestSerializer,
    UserSerializer,
    DonorSerializer,
    BloodCollectionSerializer,
    AccountSerializer,
    UserCreateSerializer,
    UserLogoutSerializer,
    GetDonorSerializer,
    DonatedDateUpdateSerializer,
    NotificationSerializer, ChangePasswordSerializer, AccDonUpdate)




class UserCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer


    def post (self, request, *args, **kwargs):

            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
        email = request.POST.get('email')
        password = request.POST.get('password')
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            authenticate(email=email, password=password)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_403_FORBIDDEN)


class UserLogoutAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post (self, request, *args, **kwargs):
        logout(request)
        return Response(status=HTTP_200_OK)




class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserUpdateSerializer



class GetAccountIDView(generics.ListAPIView):
    serializer_class = AccountIDSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Account.objects.filter(user=self.kwargs['pk'])


class GetDonorIDView(generics.ListAPIView):
    serializer_class = DonorIDSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Donor.objects.filter(user=self.kwargs['pk'])


class DonorDetailView(APIView):
    model = User
    serializer_class = AccDonUpdate
    permission_classes = [AllowAny]


    def post (self, request, *args, **kwargs):
        print("yh")
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
        serializer = AccDonUpdate(data = request.data)
        if serializer.is_valid(raise_exception = True):
            print("Val")
            return Response(status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_403_FORBIDDEN)




class DonateDateUpdate(generics.RetrieveUpdateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonatedDateUpdateSerializer
    permission_classes = [AllowAny]


#Getting made request list of the user
class getRequests(generics.ListCreateAPIView):
    current_time = datetime.now()
    threshold_time = current_time - timedelta(days=1)
    Request.objects.filter(time__lt=threshold_time).delete()
    serializer_class = RequestSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Request.objects.filter(user=self.kwargs['pk'])

#create requests
class RequestCreateView(generics.ListCreateAPIView):
    current_time = datetime.now()
    threshold_time = current_time - timedelta(days=90)
    Donor.objects.filter(last_donated_date__lte=threshold_time).update(capable=True)
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [AllowAny]


#detail of requests
class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [AllowAny]

# class UserAccountCreate(generics.ListAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#     permission_classes = [AllowAny]

class UserAccountDetail(generics.ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['pk'])
        return Account.objects.filter(user = user)


class UserDonorDetail(generics.ListAPIView):
    serializer_class = DonorSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['pk'])
        return Donor.objects.filter(user = user)



class getDonorsView(generics.ListAPIView):
    serializer_class = GetDonorSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Donor.objects.filter(bloodGroup =self.kwargs['pk'])


class BloodCollectionView(generics.ListAPIView):
    queryset = Blood.objects.all()
    serializer_class = BloodCollectionSerializer
    permission_classes = [AllowAny]


class BloodCollectionUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Blood.objects.all()
    serializer_class = BloodCollectionSerializer
    permission_classes = [AllowAny]


class NotificationDetail(generics.RetrieveUpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [AllowAny]

class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [AllowAny]

    def post (self, request, *args, **kwargs):

            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
        serializer = ChangePasswordSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            return Response(status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_403_FORBIDDEN)

