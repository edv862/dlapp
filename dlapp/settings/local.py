from .base import *  # noqa


ADMINS = (
    ('Edgar Valderrama', 'evalderrama862@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dlapp',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# You might want to use sqlite3 for testing in local as it's much faster.
if IN_TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/dlapp_test.db',
        }
    }
