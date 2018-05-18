"""myproject URL Configuration

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
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from bloodonor import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from api import views as apiview


router = DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^$', views.home, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^signup/$', views.donor_signup, name='signup'),
    url(r'^hospital_signup/$', views.hospital_signup, name='hospital_signup'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^accounts/profile/$', login_required(views.profile), name='home'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
 #   url(r'^notifications/', include('notify.urls', 'notifications')),
#   url(r'^req_notify/$', views.request_notify)
#    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    #url(r'^', RedirectView.as_view(permanent=True, url='/bloodonor/home/'), name='home' ),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'^notification/$', views.notification, name='notify'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)