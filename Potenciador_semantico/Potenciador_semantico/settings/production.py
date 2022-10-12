#necesitamos archivo base.py
from .base import *


DEBUG = False


ALLOWED_HOSTS = ['proyectogrado1.herokuapp.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dhfeif0hvurlk',
        'USER': 'ezggfhvqznsror',
        'PASSWORD': '35bae41c4e1e8e31c6efb53968758ac4a2cfb0052977b8e16d54758a0d89df80',
        'HOST': 'ec2-54-170-90-26.eu-west-1.compute.amazonaws.com',
        'DATABASE_PORT': '5432'

    }
}
