import boto3

from yumelink import settings


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


def upload_image_to_s3(local_file_path, s3_path):
    """Upload an image to S3."""
    try:
        s3_client.upload_file(local_file_path, BUCKET_NAME, s3_path)
        print(f"File uploaded successfully to {s3_path}")
        return f"https://{BUCKET_NAME}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{s3_path}"
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None


def delete_image_from_s3(s3_path):
    """Delete an image from S3."""
    try:
        s3_client.delete_object(Bucket=BUCKET_NAME, Key=s3_path)
        print(f"File {s3_path} deleted successfully")
    except Exception as e:
        print(f"Error deleting file: {e}")
