from .base import *
import os

# DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"
DEBUG = True

# ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
AUTH_USER_MODEL = []

# визначає список хостів або доменів, з яких дозволено обробляти запити до сервера.
# Це важливий механізм безпеки для запобігання атак типу HTTP Host Header Attack.
# В нашому випадку ми вписуємо "localhost", тому що наш браузер відображає http://localhost:8000/ ,
# але якщо б браузер відображав би http://123.0.0.1:8000/, то треба вписати ALLOWED_HOSTS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
