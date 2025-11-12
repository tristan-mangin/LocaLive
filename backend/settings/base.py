"""
BASE SETTINGS
-------------
This file defines the shared settings used by all environments
(dev, production, testing). Environment-specific overrides live
in dev.py and prod.py.

Structure:
    - Environment handling
    - Installed apps
    - Middleware
    - Templates
    - Database config
    - Authentication
    - REST framework
    - Static & media files
    - CORS
    - JWT
    - Logging
"""

import os
from pathlib import Path
from datetime import timedelta
from decouple import config
import dj_database_url

# BASE_DIR is the root of your Django project (one level up from 'settings/')
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ENVIRONMENT VARIABLES
# Using python-decouple lets you securely manage sensitive values in a .env file.
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", default="localhost,127.0.0.1", 
    cast=lambda v: [s.strip() for s in v.split(",")]
)

# APPLICATIONS
INSTALLED_APPS = [
    # Django core apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",               # Django REST Framework for API creation
    "corsheaders",                  # Handle CORS for React Native front end
    "rest_framework_simplejwt",     # JWT authentication for mobile apps

    # Your custom apps
    "users",                        # User accounts, profiles, authentication
    # "social",                       # Social media features (posts, likes, etc.)
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Enables serving static files efficiently (used in production with WhiteNoise)
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    # Must be placed before CommonMiddleware for CORS to work correctly
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        # Required for Django admin and template rendering
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Where Django should look for global templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        # Load templates from installed apps (like admin, auth, etc.)
        'APP_DIRS': True,

        # Template context processors provide context data globally (e.g., request object)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# URLS & WSGI
ROOT_URLCONF = "backend.urls"
WSGI_APPLICATION = "backend.wsgi.application"

# DATABASE
# Uses dj-database-url to parse a single DATABASE_URL variable from .env.
DATABASES = {
    "default": dj_database_url.parse(
        config("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
    )
}

# AUTHENTICATION
# Use a custom user model to easily add profile fields later
AUTH_USER_MODEL = "users.CustomUser"

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# REST FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

# JWT CONFIGURATION
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),   # Access token lifetime
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),      # Refresh token lifetime
    "ROTATE_REFRESH_TOKENS": True,                    # Issue new refresh token each time
    "BLACKLIST_AFTER_ROTATION": True,                 # Old refresh tokens become invalid
}

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# STATIC AND MEDIA FILES
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"     # where collectstatic will gather files

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"            # for user-uploaded content

# CORS CONFIGURATION
CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS",
    default="http://localhost:19006,http://127.0.0.1:19006",
    cast=lambda v: [s.strip() for s in v.split(",")],
)
CORS_ALLOW_CREDENTIALS = True  # Allows cookies/auth headers for cross-origin requests

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        # Sends log output to the console (visible in terminal/Docker logs)
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",  # Change to DEBUG for verbose output during development
    },
}

# DEFAULT AUTO FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ADMIN_SITE_HEADER = "LocaLive Admin"
ADMIN_SITE_TITLE = "LocaLive Admin Portal"
ADMIN_INDEX_TITLE = "Welcome to the LocaLive Dashboard"

# Media files (user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
