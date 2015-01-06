SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
    "simpleapi",
]

DATABASES = {
    "default": {
        'NAME': ':memory:',
        "ENGINE": "django.db.backends.sqlite3",
    }
}

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'tests.urls'

SIMPLEAPI_ENABLE_CORS = True
CORS_ORIGIN_ALLOW_ALL = False
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://).*$', )
