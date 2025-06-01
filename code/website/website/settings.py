import os

from pathlib import Path
from website import is_true, split_with_comma

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
INSECURE_KEY = "django-insecure-0eikswwglid=ukts4l2_b=676m!-q_%154%2z@&l3)n6)cp3#c"
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", INSECURE_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = is_true(os.getenv("DJANGO_DEBUG", "true"))

# Hosts and internal IPs
ALLOWED_HOSTS = split_with_comma(
    os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost")
)
INTERNAL_IPS = ["127.0.0.1"]

if DEBUG:
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

    # **DEV OVERRIDES: allow any host + disable CSRF-origin checks**
    ALLOWED_HOSTS = ["*"]
    CSRF_TRUSTED_ORIGINS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "mymedic_patients"
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "website.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

CORS_ALLOW_ALL_ORIGINS = True

WSGI_APPLICATION = "website.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(os.getenv("DJANGO_SQLITE_DIR", ".")) / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = os.getenv("DJANGO_LANGUAGE_CODE", "en-us")
TIME_ZONE = os.getenv("DJANGO_TIME_ZONE", "UTC")
USE_I18N = True
USE_TZ = True

# Media files
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", "")
MEDIA_URL = os.getenv("DJANGO_MEDIA_URL", "/media/")

# Static files
STATIC_URL  = "/static/"
STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", "/usr/share/nginx/html/static")
STATICFILES_DIRS = [BASE_DIR / "static"]

# Sessions and CSRF cookies (flags overridden later based on DEBUG)
SESSION_COOKIE_SECURE = is_true(os.getenv("DJANGO_SESSION_COOKIE_SECURE", "False"))
CSRF_COOKIE_SECURE = is_true(os.getenv("DJANGO_CSRF_COOKIE_SECURE", "False"))
# CSRF_TRUSTED_ORIGINS already set above in DEBUG-block if needed

# Security settings
SECURE_SSL_REDIRECT = is_true(os.getenv("DJANGO_SECURE_SSL_REDIRECT", "False"))
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# HSTS and secure cookies configuration
if DEBUG:
    # Disable HTTPS redirect and HSTS in development
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
else:
    # Production defaults
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 2  # 2 weeks
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Email settings
EMAIL_HOST = os.getenv("DJANGO_EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.getenv("DJANGO_EMAIL_PORT", 25))
EMAIL_HOST_USER = os.getenv("DJANGO_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("DJANGO_EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = is_true(os.getenv("DJANGO_EMAIL_USE_TLS", "False"))

# Default email addresses
SERVER_EMAIL = os.getenv("DJANGO_SERVER_EMAIL", "root@localhost")
DEFAULT_FROM_EMAIL = os.getenv("DJANGO_DEFAULT_FROM_EMAIL", "webmaster@localhost")

# Admin notifications
ADMIN_NAME = os.getenv("DJANGO_ADMIN_NAME", "")
ADMIN_EMAIL = os.getenv("DJANGO_ADMIN_EMAIL", "")
if ADMIN_EMAIL:
    ADMINS = [(ADMIN_NAME, ADMIN_EMAIL)]

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} [{asctime}] -- {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            # In development just log to console
            "handlers": ["console"] if DEBUG else ["mail_admins", "console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
