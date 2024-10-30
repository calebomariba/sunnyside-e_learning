from .base import *


DEBUG = False


ADMINS = [
    ('calebomariba', 'calebomariba1993@gmail.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        NAME: BASE_DIR / 'db.sqlite3',
    }
}