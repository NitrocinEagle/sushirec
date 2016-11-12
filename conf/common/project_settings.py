import os

from .auth_backends import PROJECT_AUTH_BACKENDS
from .middlewares import PROJECT_MIDDLEWARES
from conf.common.context_processors import PROJECT_CONTEXT_PROCESSORS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Russian'),
)
TIME_ZONE = 'Asia/Krasnoyarsk'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MONGO_DB_NAME = "sushirec"

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'GET', 'POST', 'OPTIONS',
)

AUTHENTICATION_BACKENDS = [] + PROJECT_AUTH_BACKENDS


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
] + PROJECT_MIDDLEWARES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ] + PROJECT_CONTEXT_PROCESSORS,
        },
    },
]

AUTH_PASSWORD_VALIDATORS = None

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

STATIC_ROOT = os.path.join(BASE_DIR, 'www/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'www/data')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'