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
