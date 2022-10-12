#necesitamos archivo base.py
from .base import *


DEBUG = True


ALLOWED_HOSTS = ['localhost', '127.0.0.1']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbofficial',
        'USER': 'postgres',
        'PASSWORD': 'elkinR340',
        'HOST': 'localhost',
        'DATABASE_PORT': '5432'

    }
}
