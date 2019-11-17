import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['monbird.com', 'monptasz.com']

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'carb_count',
         'USER': 'monbird',
         'PASSWORD': '9_raaDI0_sM3Ll__1',
         'HOST': 'localhost',
         'PORT': '3306',
     }
}

STATIC_ROOT = os.path.join(BASE_DIR, '../static')
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
