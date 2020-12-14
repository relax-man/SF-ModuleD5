from .base import *


SECRET_KEY = '21@0w$4t*7@q6gn#^7w*#*aq=_c0ttqv-l_-x2##=_t@3tkg6q'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hiianosdu',
    'API_KEY': '613229427197363',
    'API_SECRET': 'd5UL3l16e15WMRQ6qZKK1pPNcCk',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
