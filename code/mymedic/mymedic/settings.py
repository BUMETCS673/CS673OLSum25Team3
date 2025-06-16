import os
from pathlib import Path
from dotenv import load_dotenv
from mymedic import is_true

load_dotenv()

def split_with_comma(s: str):
    return [part.strip() for part in s.split(",") if part.strip()]

BASE_DIR = Path(__file__).resolve().parent.parent
INSECURE_KEY = 'django-insecure-8nk@m)abtpw$+3zxm028g18+@o4w0ig%@k!t9-zckbdre@bv5b'
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", INSECURE_KEY)
DEBUG = is_true(os.getenv("DJANGO_DEBUG", "false"))

ALLOWED_HOSTS = split_with_comma(
    os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,localhost:8080")
)
CSRF_TRUSTED_ORIGINS = split_with_comma(
    os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "")
)

_default_host = ALLOWED_HOSTS[0] if ALLOWED_HOSTS else "localhost"
_scheme = os.getenv("FRONTEND_SCHEME", "http")
FRONTEND_URL = os.getenv("FRONTEND_URL", f"{_scheme}://{_default_host}")

INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mymedic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'users' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mymedic.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': BASE_DIR / os.getenv('SQL_DATABASE', 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = os.getenv('DJANGO_LANGUAGE_CODE', 'en-us')
TIME_ZONE     = os.getenv('DJANGO_TIME_ZONE', 'UTC')
USE_I18N      = True
USE_TZ        = True

STATIC_URL  = '/static/'
STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", "/usr/share/nginx/html/static")
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND      = os.getenv(
    "DJANGO_EMAIL_BACKEND",
    "django.core.mail.backends.console.EmailBackend" if DEBUG else "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST         = os.getenv("DJANGO_EMAIL_HOST", "localhost")
EMAIL_PORT         = int(os.getenv("DJANGO_EMAIL_PORT", 25))
EMAIL_HOST_USER    = os.getenv("DJANGO_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD= os.getenv("DJANGO_EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS      = is_true(os.getenv("DJANGO_EMAIL_USE_TLS", "False"))
EMAIL_USE_SSL      = is_true(os.getenv("DJANGO_EMAIL_USE_SSL", "False"))
DEFAULT_FROM_EMAIL = os.getenv("DJANGO_DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
SERVER_EMAIL       = os.getenv("DJANGO_SERVER_EMAIL", DEFAULT_FROM_EMAIL)

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

CORS_ALLOW_ALL_ORIGINS = True
