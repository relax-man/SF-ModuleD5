from .base import *
import os


SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['.herokuapp.com']
DEBUG = False

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hiianosdu',
    'API_KEY': os.environ.get('CLOUDINARY_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
