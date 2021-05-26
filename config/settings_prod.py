from .settings import *
import os


DEBUG = int(os.getenv('DEBUG', default=0))

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS += os.getenv('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', default='5432'),
    }
} 