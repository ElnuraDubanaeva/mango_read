from decouple import config

#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": config("DB_NAME"),
#         "USER": config("DB_USER"),
#         "PASSWORD": config("DB_PASSWORD"),
#         "HOST": config("DB_HOST"),
#         "PORT": config("DB_PORT"),
#     }
# }

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
    {
        "NAME": "api.users.validators.UppercaseValidator",
    },
    {
        "NAME": "api.users.validators.SpecialCharValidator",
    },
    {
        "NAME": "api.users.validators.IsIncludeOneDigit",
    },
    {
        "NAME": "api.users.validators.IsIncludeOnlyLatn",
    },
]
