"""
DEVELOPMENT SETTINGS
--------------------
Overrides the base settings for local development.
Includes debug mode, local database, and permissive CORS.
"""

from .base import *

# Enable debug mode (never use this in production!)
DEBUG = True

# Allow your local environment only
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Use a lightweight SQLite database for development if none is specified
if DATABASES["default"]["ENGINE"] != "django.db.backends.sqlite3":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Relaxed CORS for local testing (Expo, React Native, etc.)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:19006",
    "http://127.0.0.1:19006",
]
