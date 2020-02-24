from . import *


DEBUG = False
ALLOWED_HOSTS = ['204.48.26.176']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'projet8',
        'USER': 'nathansql',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}
