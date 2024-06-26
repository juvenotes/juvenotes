import os
from datetime import timedelta

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from decouple import config
from dj_database_url import parse as db_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)


SITE_ID = 1

DEBUG = True

ADMINS = (("Admin", "developers@juvenotes.com"),)

AUTH_USER_MODEL = "users.User"

ALLOWED_HOSTS = []

# if os.getenv('DJANGO_SETTINGS_MODULE') != 'juvenotes.settings.production':
#     DATABASES = {
#         "default": config("DATABASE_URL", cast=db_url),
#     }

INSTALLED_APPS = [
    # "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_js_reverse",
    "webpack_loader",
    "import_export",
    "rest_framework",
    "rest_framework.authtoken",
    # "rest_framework_simplejwt",
    "drf_spectacular",
    "defender",
    "django_guid",
    "anymail",
    "rest_framework_simplejwt.token_blacklist",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    # all auth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    # Local apps
    "common",
    "users",
    "mcq",
    "library",
    "explanation",
]

REST_AUTH = {
    "LOGIN_SERIALIZER": "dj_rest_auth.serializers.LoginSerializer",
    "TOKEN_SERIALIZER": "dj_rest_auth.serializers.TokenSerializer",
    "JWT_SERIALIZER": "dj_rest_auth.serializers.JWTSerializer",
    "JWT_SERIALIZER_WITH_EXPIRATION": "dj_rest_auth.serializers.JWTSerializerWithExpiration",
    "JWT_TOKEN_CLAIMS_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "USER_DETAILS_SERIALIZER": "dj_rest_auth.serializers.UserDetailsSerializer",
    "PASSWORD_RESET_SERIALIZER": "dj_rest_auth.serializers.PasswordResetSerializer",
    "PASSWORD_RESET_CONFIRM_SERIALIZER": "dj_rest_auth.serializers.PasswordResetConfirmSerializer",
    "PASSWORD_CHANGE_SERIALIZER": "dj_rest_auth.serializers.PasswordChangeSerializer",
    "REGISTER_SERIALIZER": "dj_rest_auth.registration.serializers.RegisterSerializer",
    "REGISTER_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    # 'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',
    "TOKEN_MODEL": None,
    "TOKEN_CREATOR": "dj_rest_auth.utils.default_create_token",
    "PASSWORD_RESET_USE_SITES_DOMAIN": False,
    "OLD_PASSWORD_FIELD_ENABLED": False,
    "LOGOUT_ON_PASSWORD_CHANGE": True,
    "SESSION_LOGIN": True,
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "juvenotes-auth",
    "JWT_AUTH_REFRESH_COOKIE": "refresh-token",
    "JWT_AUTH_REFRESH_COOKIE_PATH": "/",
    "JWT_AUTH_SECURE": True,
    "JWT_AUTH_HTTPONLY": False,
    "JWT_AUTH_SAMESITE": "Lax",
    "JWT_AUTH_RETURN_EXPIRATION": False,
    "JWT_AUTH_COOKIE_USE_CSRF": False,
    "JWT_AUTH_COOKIE_ENFORCE_CSRF_ON_UNAUTHENTICATED": False,
}

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "users.serializers.UserSerializer",
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django_permissions_policy.PermissionsPolicyMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
    "defender.middleware.FailedLoginMiddleware",
    "django_guid.middleware.guid_middleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "juvenotes.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [base_dir_join("templates")],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "common.context_processors.sentry_dsn",
                "common.context_processors.commit_sha",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                ),
            ],
        },
    },
]

WSGI_APPLICATION = "juvenotes.wsgi.application"

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
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

REST_USE_JWT = True

# djangorestframework-simplejwt
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    # "TOKEN_OBTAIN_SERIALIZER": "custom.serializers.MyTokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

# Django-allauth
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# all-auth
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": config("GOOGLE_CLIENT_ID"),
            "secret": config("GOOGLE_SECRET"),
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "VERIFIED_EMAIL": True,
    },
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# Unfold@
UNFOLD = {
    "SITE_HEADER": _("Juvenotes Admin Site - Manage Resources"),
    "SITE_TITLE": _("Juvenotes Admin Site"),
}

# drf-spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "Juvenotes API",
    "DESCRIPTION": "Endpoints to manage our application",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True


USE_TZ = True

# STATICFILES_DIRS = (base_dir_join("../frontend"),)

# Webpack
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": False,  # on DEBUG should be False
        "STATS_FILE": base_dir_join("../webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}

# Celery
# Recommended settings for reliability: https://gist.github.com/fjsj/da41321ac96cf28a96235cb20e7236f6
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_ACKS_LATE = True
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_TRANSPORT_OPTIONS = {"confirm_publish": True, "confirm_timeout": 5.0}
CELERY_BROKER_POOL_LIMIT = config("CELERY_BROKER_POOL_LIMIT", cast=int, default=1)
CELERY_BROKER_CONNECTION_TIMEOUT = config(
    "CELERY_BROKER_CONNECTION_TIMEOUT", cast=float, default=30.0
)
CELERY_REDIS_MAX_CONNECTIONS = config(
    "CELERY_REDIS_MAX_CONNECTIONS", cast=lambda v: int(v) if v else None, default=None
)
CELERY_TASK_ACKS_ON_FAILURE_OR_TIMEOUT = config(
    "CELERY_TASK_ACKS_ON_FAILURE_OR_TIMEOUT", cast=bool, default=True
)
CELERY_TASK_REJECT_ON_WORKER_LOST = config(
    "CELERY_TASK_REJECT_ON_WORKER_LOST", cast=bool, default=False
)
CELERY_WORKER_PREFETCH_MULTIPLIER = config("CELERY_WORKER_PREFETCH_MULTIPLIER", cast=int, default=1)
CELERY_WORKER_CONCURRENCY = config(
    "CELERY_WORKER_CONCURRENCY", cast=lambda v: int(v) if v else None, default=None
)
CELERY_WORKER_MAX_TASKS_PER_CHILD = config(
    "CELERY_WORKER_MAX_TASKS_PER_CHILD", cast=int, default=1000
)
CELERY_WORKER_SEND_TASK_EVENTS = config("CELERY_WORKER_SEND_TASK_EVENTS", cast=bool, default=True)
CELERY_EVENT_QUEUE_EXPIRES = config("CELERY_EVENT_QUEUE_EXPIRES", cast=float, default=60.0)
CELERY_EVENT_QUEUE_TTL = config("CELERY_EVENT_QUEUE_TTL", cast=float, default=5.0)

# Sentry
SENTRY_DSN = config("SENTRY_DSN", default="")
COMMIT_SHA = config("RENDER_GIT_COMMIT", default="")

# Fix for Safari 12 compatibility issues, please check:
# https://github.com/vintasoftware/safari-samesite-cookie-issue
CSRF_COOKIE_SAMESITE = None
SESSION_COOKIE_SAMESITE = None

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# All available policies are listed at:
# https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md
# Empty list means the policy is disabled
PERMISSIONS_POLICY = {
    "accelerometer": [],
    "camera": [],
    "display-capture": [],
    "encrypted-media": [],
    "geolocation": [],
    "gyroscope": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "payment": [],
    "usb": [],
    "xr-spatial-tracking": [],
}

# Django-CSP
CSP_INCLUDE_NONCE_IN = ["script-src", "style-src", "font-src"]
CSP_SCRIPT_SRC = [
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "https://browser.sentry-cdn.com",
    # drf-spectacular UI (Swagger and ReDoc)
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/",
    "https://cdn.jsdelivr.net/npm/redoc@latest/",
    "blob:",
] + [f"*{host}" if host.startswith(".") else host for host in ALLOWED_HOSTS]
CSP_CONNECT_SRC = [
    "'self'",
    "*.sentry.io",
] + [f"*{host}" if host.startswith(".") else host for host in ALLOWED_HOSTS]
CSP_STYLE_SRC = [
    "'self'",
    "'unsafe-inline'",
    # drf-spectacular UI (Swagger and ReDoc)
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/",
    "https://cdn.jsdelivr.net/npm/redoc@latest/",
    "https://fonts.googleapis.com",
]
CSP_FONT_SRC = [
    "'self'",
    "'unsafe-inline'",
    # drf-spectacular UI (Swagger and ReDoc)
    "https://fonts.gstatic.com",
] + [f"*{host}" if host.startswith(".") else host for host in ALLOWED_HOSTS]
CSP_IMG_SRC = [
    "'self'",
    # drf-spectacular UI (Swagger and ReDoc)
    "data:",
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/",
    "https://cdn.redoc.ly/redoc/",
]

# Django-defender
# DEFENDER_LOGIN_FAILURE_LIMIT = 3
# DEFENDER_COOLOFF_TIME = 300  # 5 minutes
# DEFENDER_LOCKOUT_TEMPLATE = "defender/lockout.html"
# DEFENDER_REDIS_URL = config("REDIS_URL")
