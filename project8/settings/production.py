from . import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False
ALLOWED_HOSTS = ['204.48.26.176']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projet8',
        'USER': 'nathansql',
        'PASSWORD': 'nathan',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

sentry_sdk.init(
    dsn="https://0b44cc663eaa4f35b107cbdd75719913@sentry.io/2827010",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
