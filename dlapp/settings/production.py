from .base import *  # noqa
import os


DEBUG = False
TEMPLATES[0]['debug'] = DEBUG

SECRET_KEY = os.environ.get("SECRET_KEY", "ev_%z7docsxs@+_amp48qx@j!z3+vtf$=#ejx#lq)g2@xhv2h!")

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

ADMINS = (
    ('Edgar Valderrama', 'evalderrama862@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dlapp',
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': '',
    }
}

STATIC_ROOT = '/static/'
