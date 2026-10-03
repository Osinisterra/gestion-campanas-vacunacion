import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,backend"
).split(",")
ROOT_URLCONF = "config.urls"
INSTALLED_APPS = ["rest_framework"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("DATABASE_PATH", "/data/development.sqlite3"),
    }
}
REST_FRAMEWORK = {"UNAUTHENTICATED_USER": None, "DEFAULT_AUTHENTICATION_CLASSES": []}
LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_TZ = True
