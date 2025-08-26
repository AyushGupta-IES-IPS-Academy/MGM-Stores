from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class PublicSupabaseStorage(S3Boto3Storage):
    """
    Custom storage that forces public Supabase bucket URLs
    instead of signed URLs.
    """
    def url(self, name):
        return f"{settings.MEDIA_URL}{name}"