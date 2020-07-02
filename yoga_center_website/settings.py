"""
Django settings for yoga_center_website project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import dj_database_url
import os
from getenv import env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0sd=iuk$&h6r26msa=b+v%a2#tqm_8#8s#8g!!0_n1!4jk(x%@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['yogahuongtre.herokuapp.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django_countries',
    'crispy_forms',
    'tempus_dominus',
    'rest_framework',
    'formtools',
    'ckeditor',
    'ckeditor_uploader',
    'dynamic_formsets',
    'django_twilio',
    'qr_code',

    'apps.accounts',
    'apps.common',
    'apps.profiles',
    'apps.home',
    'apps.courses',
    'apps.classes',
    'apps.lessons',
    'apps.lectures',
    'apps.rooms',
    'apps.cards',
    'apps.card_types',
    'apps.yoga_schedule',
    'apps.card_invoices',
    'apps.dashboard',
    'apps.roll_calls',
    'apps.trainers',
    'apps.blog',
    'apps.make_up_lessons',
    'apps.refunds',
    'apps.shop',
    'apps.promotions',
    'apps.errors',
    'apps.events',
    'apps.faq',
    'apps.questions',
    'apps.feedback',
    'apps.donations',
    'apps.absence_applications',
    'seeds',
    'notifications'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'yoga_center_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yoga_center_website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGES = [('vi', 'VN')]

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

LANGUAGE_CODE = 'vi'

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Extra lookup directories for collectstatic to find static files
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SITE_ID = 1

# Custom Auth User model
AUTH_USER_MODEL = 'accounts.User'

# Custom Auth User model
AUTH_USER_MODEL = 'accounts.User'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Skip Email Verification
ACCOUNT_EMAIL_VERIFICATION = 'none'

# CRISPY
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/'

TEMPUS_DOMINUS_LOCALIZE = True

FORMAT_MODULE_PATH = 'yoga_center_website.formats'

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'CMS',
        'toolbar_CMS': [
            {
                'name': 'basicstyles',
                'groups': ['basicstyles', 'cleanup'],
                'items': ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat']
            },
            {
                'name': 'paragraph',
                'groups': ['list', 'indent', 'blocks'],
                'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']
            },
            {
                'name': 'links',
                'items': ['Link', 'Unlink']
            },
            {
                'name': 'insert',
                'items': ['Image', 'HorizontalRule', 'Table', 'Iframe', ]
            },
            {
                'name': 'colors',
                'items': ['TextColor', 'BGColor']
            },
            {
                'name': 'insert',
                'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']
            },
            {
                'name': 'youtube',
                'items': ['Youtube', ]
            },
            {
                'name': 'tools',
                'items': ['Maximize', 'ShowBlocks']
            },
            {
                'name': 'styles',
                'items': ['Styles', 'Format', 'Font', 'FontSize']
            },
            {
                'name': 'document',
                'items': ['Source']
            },
        ],
        'height': '200px',
        'width': '100%',
        'extraPlugins': 'youtube',
    }
}

SESSION_SAVE_EVERY_REQUEST = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_USE_SLL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL')
EMAIL_HOST_PASSWORD = env('PASSWORD')

TWILIO_ACCOUNT_SID = env('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = env('TWILIO_AUTH_TOKEN')
DEFAULT_TO_NUMBER = env('DEFAULT_TO_NUMBER')
TWILIO_PHONE_NUMBER = env('TWILIO_PHONE_NUMBER')

STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')

# env link
YOGA_CENTER_YOUTUBE_URL = env('YOGA_CENTER_YOUTUBE_URL')
YOGA_CENTER_FACEBOOK_URL = env('YOGA_CENTER_FACEBOOK_URL')
TAWK_TO_API_URL = env('TAWK_TO_API_URL')
FACEBOOK_PRIVACY_POLICY_URL = str(env('FACEBOOK_PRIVACY_POLICY_URL'))

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

# EXPIRE TIME (MONTH) OF LESSON
# To register make-up lessons or make a refund
NUMBER_OF_EXPIRE_DAYS_FOR_LESSON = 30

MIN_PERCENTAGE_LESSONS_TO_REGISTER = 0.25

MAX_NUMBER_OF_MAKE_UP_LESSONS_PERCENTAGE = 0.25

MOMO_ACCESS_KEY = "aLGGNpsO3HcSPkqQ"
MOMO_SECRET_KEY = "w84mB5zTLehWMUqPNvnWuvqg5S2DkUfH"
MOMO_PARTNER_CODE = "MOMONZWN20200513"
MOMO_END_POINT = "https://test-payment.momo.vn/gw_payment/transactionProcessor"

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://127.0.0.1:6379')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379')

MINUTES_TO_REMOVE_UNPAID_CARD = int(os.getenv('MINUTES_TO_REMOVE_UNPAID_CARD', 7 * 24 * 60))
