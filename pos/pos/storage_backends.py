from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class PublicSupabaseStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    custom_domain = f"https://{settings.SUPABASE_PROJECT_REF}.supabase.co/storage/v1/object/public/{settings.AWS_STORAGE_BUCKET_NAME}"
    default_acl = "public-read"
    querystring_auth = False  # important for public buckets
