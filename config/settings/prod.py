from .base import *

DEBUG = False

assert SECRET_KEY is not None, (
    'Please provide DJANGO_SECRET_KEY' 
    'Environment variable with value'
)

# DATABASES['default'].update({
#         'NAME': config('DB_NAME'),
#         'HOST': config('DB_HOST'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'PORT': 5432,
# })


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
