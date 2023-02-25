from decouple import config

from .base import *

DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db1.sqlite3",
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 12,
    "NON_FIELD_ERRORS_KEY": "error",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
}
