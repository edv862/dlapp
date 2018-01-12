from .base import *  # noqa
import os


DEBUG = False
TEMPLATES[0]['debug'] = DEBUG

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

ADMINS = (
    ('Edgar Valderrama', 'evalderrama862@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'dlapp',
    #     'USER': os.environ.get('DB_USER', ''),
    #     'PASSWORD': os.environ.get('DB_PASSWORD', ''),
    #     'HOST': os.environ.get('DB_HOST', ''),
    #     'PORT': '',
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dlapp.db',
    }
}

STATIC_ROOT = root('static')
