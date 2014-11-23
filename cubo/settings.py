"""
Django settings for cubo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = "9($awd^oxek2+s-wtho=%eh=e7+%1g$@wa5g)8rs%hvm4++#vt"

# SECURITY WARNING: don"t run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"centros",
	"clientes",
	"compras",
	"contactos",
	"cotizaciones",
	"equipos",
	"familias",
	"historiales",
	"lugares",
	"productos",
	"proveedores",
	"solicitudes",
	"tastypie",
	"tiposequipos",
	"usuarios"
)

MIDDLEWARE_CLASSES = (
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.auth.middleware.SessionAuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
	"middleware.crossdomainxhr.XsSharing"
)

ROOT_URLCONF = "cubo.urls"

WSGI_APPLICATION = "cubo.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": "d2on6c3oiju1fo",
		"USER": "nzqbjckyizormr",
		"PASSWORD": "yf6Qa5lM0Uvb4SgxGHzPlHffcN",
		"HOST": "ec2-54-204-38-16.compute-1.amazonaws.com",
		"PORT": "5432"
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = "/static/"

####################### HEROKU CONFIG #######################

# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES["default"] =  dj_database_url.config()

# Honor the "X-Forwarded-Proto" header for request.is_secure()

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Allow all host headers

ALLOWED_HOSTS = ["*"]

# XS

XS_SHARING_ALLOWED_ORIGINS = "*"
XS_SHARING_ALLOWED_METHODS = ["POST", "GET", "OPTIONS", "PUT", "DELETE"]