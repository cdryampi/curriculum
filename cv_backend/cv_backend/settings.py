"""
Django settings for cv_backend project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!



SECRET_KEY = config('SECRET_KEY', default='unsafe-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

URL_SERVER = config('URL_SERVER', default='http://localhost:8000')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django_recaptcha',
    'projects',
    'coment',
    'colorfield',
    'corsheaders',
    'cv_backend',
    'base_user',
    'services',
    'experiencia_laboral',
    'core',
    'redes_sociales',
    'multimedia_manager',
    'django_ckeditor_5',
    'static_pages',
    'education_and_skills',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'cv_backend.urls'

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

WSGI_APPLICATION = 'cv_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['undo', 'redo', '|', 'heading', '|', 'bold', 'italic', 'strikethrough', 'underline', 'link', 'bulletedList', 'numberedList', '|', 'outdent', 'indent', '|', 'blockQuote', 'insertTable', 'mediaEmbed', 'imageUpload', '|', 'removeFormat', 'sourceEditing'],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:inline', 'imageStyle:block', 'imageStyle:side']
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells']
        },
        'simpleUpload': {
            'uploadUrl': 'URL_TO_YOUR_UPLOAD_ENDPOINT',  # Asegúrate de configurar un endpoint para la carga de imágenes
            'headers': {
                'X-CSRFToken': 'CSRF_TOKEN'  # Usar el token CSRF correcto aquí
            }
        },
        'height': '400px',
        'width': 'auto',
    },
    'extends': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', '|', 'blockQuote', 'CKFinder', 'imageUpload', 'undo', 'redo'],
        'image': {
            'toolbar': ['imageStyle:full', 'imageStyle:side', '|', 'imageTextAlternative']
        },
        'ckfinder': {
            'uploadUrl': '/ckfinder_connector/',  # Asegúrate de configurar correctamente la URL de subida
        },
        'height': '400px',
        'width': 'auto',
        'extraPlugins': ','.join([
            'uploadimage',  # Permite la subida de imágenes
            'divarea',      # Mejora la edición de la estructura del documento
            'ckeditor_wiris'  # Plugin para fórmulas matemáticas, si es necesario
        ]),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-es'  # Para español de España, usa 'es' para español genérico
TIME_ZONE = 'Europe/Madrid'  # Ajusta a tu zona horaria local

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Personalización del admin

JAZZMIN_SETTINGS = {
    "site_title": "Admin de Mi Currículum",
    "site_header": "Mi Currículum",
    "site_brand": "Mi Currículum",
    "welcome_sign": "Bienvenido al Panel de Administración",
    "search_model": "auth.User",
    "user_avatar": None,  # Personaliza esto según tus necesidades
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY', default='6Lccat8pAAAAAFT2Xlgt0STyZHYVM2_WP5oYLj1')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY', default='6Lccat8pAAAAAFT2Xlgt0STyZHYVM2_WP5oYLj1')

# settings.py
AUTH_USER_MODEL = 'base_user.CustomUser'

# logs