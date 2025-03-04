from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# визначає список хостів або доменів, з яких дозволено обробляти запити до сервера.
# Це важливий механізм безпеки для запобігання атак типу HTTP Host Header Attack.
# В нашому випадку ми вписуємо "localhost", тому що наш браузер відображає http://localhost:8000/ ,
# але якщо б браузер відображав би http://123.0.0.1:8000/, то треба вписати ALLOWED_HOSTS = ["127.0.0.1"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PGDATABASE'],
        'USER': os.environ['PGUSER'],
        'PASSWORD': os.environ['PGPASSWORD'],
        'HOST': os.environ['PGHOST'],
        'PORT': int(os.environ['PG_DB_PORT']),
    }
}