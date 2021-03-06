"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j*ihr-68bq_j#1s3=(hys4z78+4vn@2igw20^6%0guelm7#^90'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'channels',
    'bloodonor',
    'api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'social_django',
    'gcm',
    'notify',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]


ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'
ASGI_APPLICATION = "myproject.routing.application"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'bloodonor',
    'USER': 'AH420',
    'PASSWORD': 'srn_hady_420',
    'HOST': 'dbinstance.cieop9c0wvpd.us-east-2.rds.amazonaws.com',
    'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

AUTH_USER_MODEL = 'api.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# NOTIFICATIONS_SOFT_DELETE=True
# NOTIFICATIONS_USE_JSONFIELD=True
# NOTIFY_UPDATE_TIME_INTERVAL = 5000

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
SOCIAL_AUTH_GITHUB_KEY = '6f4dc580bfe6a972963b'
SOCIAL_AUTH_GITHUB_SECRET = 'a3de7696342c45a772df2432f3dcb6a8f8411c84'
SOCIAL_AUTH_TWITTER_KEY = 'iDE5EsIMOLjXOO3iaXr0RwOyL'
SOCIAL_AUTH_TWITTER_SECRET = 'VNL2HmZh9GCsGGaXBHXnMHdwIfySZhHVC8i8PyBqxCL863QFNU'
SOCIAL_AUTH_FACEBOOK_KEY = '1558776537534013'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c081ead010508442fa413b107b19050d'
GOOGLE_API_KEY = 'AIzaSyD--your-google-maps-key-SjQBE'
GCM_APIKEY = "<AIzaSyDCLjjDBPSes7ODTCimvpbUYGnZWYxpR7I>"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
       # 'rest_framework.authentication.BasicAuthentication',
       # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.

}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

'''SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 10 # set just 10 seconds to test
SESSION_SAVE_EVERY_REQUEST = True'''

ALLOWED_HOSTS = ['192.168.1.14', 'localhost', '10.0.2.2', '127.0.0.1', '138.37.227.175','138.37.226.125']
# mysite/settings.py
# Channels


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}