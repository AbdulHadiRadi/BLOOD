""" mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rest_framework_views
app_name = 'api'




urlpatterns = [
    url(r'^user/$', views.UserCreateAPIView.as_view(), name='register'),
    #url(r'^email/$', views.emailSentView.as_view(), name='email'),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserDetailAPIView.as_view(), name="user-detail"),
    url(r'^login/$', views.UserLoginAPIView.as_view(), name='in'),
    url(r'^logout/$', views.UserLogoutAPIView.as_view(), name='out'),
    url(r'^get_donorID/(?P<pk>[0-9]+)$', views.GetDonorIDView.as_view(), name='donors'),
    url(r'^donor_update/$', views.DonorDetailView.as_view(), name='donors_detail'),
    url(r'^donated_date/(?P<pk>[0-9]+)$', views.DonateDateUpdate.as_view(), name='donors_detail'),
    url(r'^get_accountID/(?P<pk>[0-9]+)$', views.GetAccountIDView.as_view(), name='acc'),
#    url(r'^account/$', views.UserAccountCreate.as_view(), name="acc_detail"),
    url(r'^account/(?P<pk>[0-9]+)$', views.UserAccountDetail.as_view(), name="acc_detail"),
    url(r'^donor/(?P<pk>[0-9]+)$', views.UserDonorDetail.as_view(), name="don_detail"),
    url(r'^getDonors/(?:(?P<pk>.+)/)?$', views.getDonorsView.as_view(), name='get_donors'),
    url(r'^request/$', views.RequestCreateView.as_view(), name='request'),
    url(r'^request/(?P<pk>[0-9]+)$', views.RequestDetailView.as_view(), name='request'),
    url(r'^get_request/(?P<pk>[0-9]+)$', views.getRequests.as_view(), name='get_request'),
    url(r'^blood_collection/$', views.BloodCollectionView.as_view(), name='blood_collection'),
    url(r'^blood_collection/(?P<pk>[0-9]+)$', views.BloodCollectionUpdateView.as_view(), name='blood_update'),
    url(r'^notify/(?P<pk>[0-9]+)$', views.NotificationDetail.as_view(), name='notify'),
    url(r'^changePassword/$', views.ChangePasswordView.as_view(), name='change'),
]


