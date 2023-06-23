import os
from pathlib import Path
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Set SECRET_KEY from environment variable
SECRET_KEY = os.getenv("SECRET_KEY", 'django-insecure-%%s3@elt%hj=-oj^hteyv61mnik14za_i!nmwle0=8%2&s-s@d')

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'muaythaiapp',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'muaythai.urls'

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

WSGI_APPLICATION = 'muaythai.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'muaythai_db',
        'USER': 'muaythai_admin',
        'PASSWORD': 'mypassword',
        'HOST': 'containers-us-west-142.railway.app',
        'PORT': '6708',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME', 'muaythai_db'),
#         'USER': os.getenv('DB_USER', 'muaythai_admin'),
#         'PASSWORD': os.getenv('DB_PASSWORD', 'mypassword'),
#         'HOST': os.getenv('DB_HOST', 'dpg-ci7u1fenqql0lde131b0-a.oregon-postgres.render.com'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'muaythai_db',
#         'USER': 'muaythai_admin',
#         'PASSWORD': 'mypassword',
#         'HOST': 'containers-us-west-45.railway.app',
#         'PORT': '6486',
#     }
# }


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'muaythai_db',
#         'USER': 'muaythai_admin',
#         'PASSWORD': 'mypassword',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('RAILWAY_DATABASE_NAME'),
#         'USER': os.getenv('RAILWAY_DATABASE_USER'),
#         'PASSWORD': os.getenv('RAILWAY_DATABASE_PASSWORD'),
#         'HOST': os.getenv('RAILWAY_DATABASE_HOST'),
#         'PORT': os.getenv('RAILWAY_DATABASE_PORT'),
#     }
# }



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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
        'DEFAULT_PARSER_CLASSES': [
            'rest_framework.parsers.JSONParser',
    ],    
}