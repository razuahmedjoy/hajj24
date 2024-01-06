from pathlib import Path
import os
from decouple import config


BASE_DIR = Path('__file__').resolve().parent.parent
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=True, cast=bool) 
# DEBUG = config("DEBUG", default=True, cast=bool)
# 'django-insecure-&-^-llk#t9^v&a+1#c)i=lzjt5bh0-af*0uw1(*jr^nry!z*1i'
# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["*"]


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5174",
    'http://192.168.56.1:8000',
    'http://192.168.56.1:8001',
]
CSRF_TRUSTED_ORIGINS = ['https://*.ngrok-free.app/', 'https://*.at.remote.it/','https://desktop-0lhsjl5-http.at.remote.it:33000', 'https://desktop-0lhsjl5-http.at.remote.it','https://desktop-0lhsjl5-http.at.remote.it:33006','http://192.168.56.1:8000','http://192.168.56.1:8001','https://*.127.0.0.1:8001', 'http://10.24.197.111:8001/', 'http://10.24.197.111:8000/']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",

    'main_app',
    'rest_framework',
    "rest_framework.authtoken",
]

AUTH_USER_MODEL = 'main_app.User'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hajj24_backend.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'hajj24_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'sql_mode': 'traditional',
            },
			'NAME': config("DATABASE_NAME"),
			'USER': config("DATABASE_USER"),
			'PASSWORD': config("PASSWORD"),
			'HOST': config("HOST"),
			'PORT': '3306'
			
		}
	}

# postgres://hajj24_user:SQiZj7QWHtENe85K1lW3nwUdOSrtUCih@dpg-clgc69njc5ks73ee87n0-a/hajj24

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
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
