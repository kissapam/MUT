"""
Django settings (példa) — helyezd a project-level mappába (pl. raktar_project/settings.py).
Szerkeszd a PROJECT_NAME / SECRET_KEY / ALLOWED_HOSTS mezőket a saját projektednek megfelelően.
"""

from pathlib import Path
import os

# BASE_DIR: project_root (ahol a manage.py is található)
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: ne hagyd nyilvánosan a SECRET_KEY-t production környezetben!
# Ajánlott: beállítani környezeti változóként (pl. export DJANGO_SECRET_KEY=...)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-placeholder-secret-key-change-me')

# DEBUG legyen False production-ben
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Alkalmazások: add hozzá a saját appod nevét (például 'raktar')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Saját alkalmazás(ok)
    'raktar',  # <- ha az appod neve 'raktar'; módosítsd ha más
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF: ügyelj arra, hogy a PROJECT_NAME modul legyen itt (pl. 'raktar_project.urls')
ROOT_URLCONF = 'project.urls'  # <-- cseréld le a projekted nevére, pl. 'raktar_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Központi templates mappa (project_root/templates) és app-level templates engedélyezve
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application (ROOT)
WSGI_APPLICATION = 'project.wsgi.application'  # <-- cseréld le a saját projekted nevére

# Egyszerű SQLite DB példa - fejlesztéshez kényelmes
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Jelszó validátorok (alap)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Nemzetközi beállítások
LANGUAGE_CODE = 'hu-hu'
TIME_ZONE = 'Europe/Budapest'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statikus fájlok (CSS, JS, képek)
STATIC_URL = '/static/'
# Fejlesztésnél, ha a static/ mappa közvetlenül a project rootban van:
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# collectstatic kimenete production-hoz
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Média fájlok (ha használsz feltöltést)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Alapértelmezett belépés/átirányítások
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Cookie / biztonság (tuning production-hoz)
CSRF_TRUSTED_ORIGINS = os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS', '').split(',') if os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS') else []

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login/Logout beállítások
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

