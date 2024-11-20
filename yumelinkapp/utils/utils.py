import boto3

from yumelink import settings

SMALL_TEXT = 100
MID_SMALL_TEXT = 500
MID_BIG_TEXT = 2000
BIG_TEXT = 5000

UNTITLED = 'Untitled'


def get_s3_client():
    """Get S3 client for authentication to access S3 storage."""
    return boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
    )


s3_client = get_s3_client()
BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME

# use s3_client to upload/delete image

def user_profile_path(instance, filename):
    return f'users/{instance.id}/{filename}'


def chatroom_profile_path(instance, filename):
    return f'chatrooms/{instance.id}/{filename}'


def post_image_upload_path(instance, filename):
    if instance.post and instance.post.user:
        return f'{instance.post.user.id}/post/{instance.post.id}/{filename}'
    return f'unknown/post/{filename}'
