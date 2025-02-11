"""
Django settings for hosteldb20 project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5f66y8s&&)c)y9fzapv@xzr$ck_c*a!ie%s%xugag3^f-7gtye'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',      ##for auto commos and ruppie symbol and chaekc duepage.html import   {% load humanize %}
    'hostelapp20',
    'django.contrib.sites',
    'social_django', #add this
    'rest_framework',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hostelapp20.middleware.social_auth_middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this

    
]
# settings.py
SESSION_COOKIE_SECURE = False  # Should be True in production with HTTPS
SESSION_EXPIRE_AT_BROWSER_CLOSE = False


#social app custom settings

import os


SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
  
]

# Use environment variables for sensitive data
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('GOOGLE_OAUTH2_SECRET')\

# LOGIN_REDIRECT_URL = 'dashboard'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard/'  # URL to redirect after login
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login_and_registration/'  # URL to redirect after a failed login

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',  # Gather details from the social provider
    'social_core.pipeline.social_auth.social_uid',      # Extract the user ID from the social provider
    'social_core.pipeline.social_auth.auth_allowed',    # Check if authentication is allowed
    'social_core.pipeline.social_auth.social_user',     # Associates current social details with a user account
    'hostelapp20.pipeline.handle_user_email',           # Custom function to handle email checks
    'social_core.pipeline.user.get_username',           # Get a username for the new user
    'social_core.pipeline.user.create_user',            # Create a new user account if one does not exist
    'social_core.pipeline.social_auth.associate_user',  # Associate the social account with the user
    'social_core.pipeline.social_auth.load_extra_data', # Load extra data from the social provider
    'social_core.pipeline.user.user_details',           # Populate the user details
)

SOCIAL_AUTH_STRATEGY = 'hostelapp20.strategies.CustomSocialStrategy'  #for this 


# ------------------------------------------------------------------------

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'


ROOT_URLCONF = 'hosteldb20.urls'
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  #dd this 

            ],
        },
    },
]

WSGI_APPLICATION = 'hosteldb20.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# settings.py

import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3'), conn_max_age=600, ssl_require=False)
}







# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')

# for sicoal authanticatuon

MEDIA_URL = '/media/'  # Ensure MEDIA_URL is distinct from STATIC_URL
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Place media files in a directory outside of STATIC_ROOT

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  ## for static folder

## if the 'auth.User', which has been swapped out  use custom user
AUTH_USER_MODEL = 'hostelapp20.CustomUser'  ## for abstract user

## Define the path to the static/media directory

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'muraliprasad996.996.mp@gmail.com'
EMAIL_HOST_PASSWORD = 'ztjh fdxk rytu vnef'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'


# ztjh fdxk rytu vnef
# Add logging



