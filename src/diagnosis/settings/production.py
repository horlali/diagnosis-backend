import os

from dotenv import load_dotenv

from diagnosis.settings.base import *

# Load environment file
ENV_DIR = BASE_DIR.parent
load_dotenv(os.path.join(ENV_DIR, ".env"))

# Debug Mode
DEBUG = False

# Secret Keys
SECRET_KEY = os.getenv("SECRET_KEY")

# Allowed host
ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB_NAME"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

# Celery settings
CELERY_BROKER_URL = os.getenv("CELERY_BROKER")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

# Redis Cache Settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv("REDIS_CACHE_URL"),
    }
}

# CORS
CORS_ALLOWED_ORIGINS = [
    os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000"),
]
