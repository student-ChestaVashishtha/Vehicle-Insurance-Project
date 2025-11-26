import boto3
import os
from src.constants import AWS_ACCESS_KEY_ID_ENV_KEY, AWS_SECRET_ACCESS_KEY_ENV_KEY, REGION_NAME

class S3Client:
    s3_client = None
    s3_resource = None

    def __init__(self, region_name=REGION_NAME):
        
        # Load once and keep available
        access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
        secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

        if not access_key_id:
            raise Exception(f"AWS Access Key Environment Variable '{AWS_ACCESS_KEY_ID_ENV_KEY}' Not Found")

        if not secret_access_key:
            raise Exception(f"AWS Secret Access Key Environment Variable '{AWS_SECRET_ACCESS_KEY_ENV_KEY}' Not Found")

        # Create boto objects only once (Singleton pattern)
        if S3Client.s3_client is None or S3Client.s3_resource is None:
            S3Client.s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name
            )
            S3Client.s3_client = boto3.client(
                "s3",
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name
            )

        # Assign class values to instance
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
