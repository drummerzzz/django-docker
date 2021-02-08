from decouple import config

if config("AWS_ACCESS_KEY", default=None):
  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
  AWS_S3_ACCESS_KEY_ID = config("AWS_ACCESS_KEY")
  AWS_S3_SECRET_ACCESS_KEY = config("AWS_SECRET_KEY_ID")
  AWS_STORAGE_BUCKET_NAME = config("BUCKET_NAME")
  AWS_DEFAULT_ACL = 'public-read'
  AWS_S3_FILE_OVERWRITE = True
  AWS_S3_REGION_NAME = config("REGION")