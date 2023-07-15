from pathlib import Path
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
FRONT_BASE_DIR = Path.joinpath(Path(__file__).resolve().parent.parent.parent, "front")

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")]
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # APPS
    # THIRD PARTY
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Required for corsheaders
    "django.middleware.common.CommonMiddleware",  # Required for corsheaders
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Tells django where to find the templates (after build is run with vite)
        "DIRS": [FRONT_BASE_DIR / "dist"],
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

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {"default": dj_database_url.config(default=config("DATABASE_URL"))}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_HEALTH_CHECKS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = 600

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ]
}

CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS", cast=lambda v: [s.strip() for s in v.split(",")]
)


CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS", cast=lambda v: [s.strip() for s in v.split(",")]
)

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "assets/"  # folder of front static assests (with vite)
MEDIA_URL = "media/"

STATICFILES_DIRS = [
    FRONT_BASE_DIR / "dist/assets",
]  # build/assets to serve files from React (build with vite)

if not DEBUG:
    DEFAULT_FROM_EMAIL = "Depp Django - <mail@deepdjango.com>"
    EMAIL_HOST = config("EMAIL_HOST", default="localhost")
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = config("EMAIL_PORT", default=25, cast=int)
    EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=False, cast=bool)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
