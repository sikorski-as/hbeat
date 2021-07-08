from .settings import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

SECRET_KEY = 'debug-secret-key'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}