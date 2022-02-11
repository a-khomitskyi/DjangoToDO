import os


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "django-todo"
AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION = "https://django-todo.fra1.digitaloceanspaces.com"
STATICFILES_STORAGE = 'DjangoToDO.cdn.backends.StaticRootS3BotoStorage'
AWS_QUERYSTRING_AUTH = False
