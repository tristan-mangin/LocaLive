"""
PRODUCTION SETTINGS
-------------------
Overrides the base settings for secure deployment.
Includes HTTPS, stricter CORS, and optimized static file handling.
"""

from .base import *

DEBUG = False

# Replace this with your domain or cloud deployment URL
ALLOWED_HOSTS = ["yourdomain.com", "api.yourdomain.com"]

# Security settings for HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Use WhiteNoise to efficiently serve static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Restrictive CORS (only your production front-end should be allowed)
CORS_ALLOWED_ORIGINS = [
    "https://yourfrontend.com",
]
