"""
MinIO object and storage management
"""
import sys

from minio import Minio, error
from pathlib import Path

try:
    client = Minio(
        "localhost:9000", access_key="minio", secret_key="minio123", secure=False
    )
except:
    print("Cannot connect to MinIO. Exiting...")
    sys.exit()


def create_bucket(bucket: str) -> None:
    """Create a new bucket"""

    # Validate func params
    if not isinstance(bucket, str):
        raise ValueError("Bucket name must be a string")

    if client.bucket_exists(bucket):
        # Doesn't re-create an existing bucket
        print(f"{bucket} exists")
    else:
        print(f"{bucket} does not exist")
        print(f"Create bucket {bucket}")

        try:
            client.make_bucket(bucket)
        except:
            print(f"Cannot create {bucket} bucket")


def object_exists(bucket: str, object_name: str) -> bool:
    """Check if an object exists"""

    # Validate func params
    if not isinstance(bucket, str):
        raise ValueError("Bucket name must be a string")
    if not isinstance(object_name, str):
        raise ValueError("Object name must be a string")

    # The bucket doesn't exists, so either does the object
    if not client.bucket_exists(bucket):
        return False

    try:
        client.stat_object(bucket, object_name)
    except error.S3Error as e:
        if e.code == "NoSuchKey":
            return False

    return True


def upload_object(bucket: str, object_name: str, file_path: str) -> None:
    """Upload a file to bucket"""

    # Validate func params
    if not isinstance(bucket, str):
        raise ValueError("Bucket name must be a string")
    if not isinstance(object_name, str):
        raise ValueError("Object name must be a string")
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string")

    # Cannot upload file to bucket due to:
    # - file doesn't exits
    # - bucket doesn't exits
    # - file already exists in bucket
    if (
        not Path(file_path).is_file()
        or not client.bucket_exists(bucket)
        or object_exists(bucket, object_name)
    ):
        print(f"Cannot upload {object_name} to {bucket} bucket due to some problems")
        return

    try:
        # Upload file
        client.fput_object(
            bucket_name=bucket, object_name=object_name, file_path=file_path
        )
        print(f"Upload {object_name} to {bucket} bucket successfully")
    except:
        print(f"Cannot upload {object_name} to {bucket} bucket")


def download_object(bucket: str, object_name: str, file_path: str) -> None:
    """Download object from bucket"""

    # Validate func params
    if not isinstance(bucket, str):
        raise ValueError("Bucket name must be a string")
    if not isinstance(object_name, str):
        raise ValueError("Object name must be a string")
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string")

    # Cannot download object because it doesn't exists
    if not object_exists(bucket, object_name):
        print(f"Cannot download {object_name} object. It doesn't exist")
        return

    try:
        # Download file
        client.fget_object(
            bucket_name=bucket, object_name=object_name, file_path=file_path
        )
        print(f"Download {object_name} in {bucket} bucket successfully")
    except:
        print(f"Cannot download {object_name} in {bucket} bucket")


def main() -> None:
    # Create buckets: bronze, silver, gold
    create_bucket("bronze")
    create_bucket("silver")
    create_bucket("gold")

    # Working with CSV, JSON, Parquet file (Read/Write)
    bucket_name = "warehouse-script"
    create_bucket(bucket_name)

    # Uploading CSV, JSON, parquet
    upload_object(bucket_name, "data.csv", "./data/data-example/data.csv")
    upload_object(bucket_name, "data.json", "./data/data-example/data.json")
    upload_object(bucket_name, "data.parquet", "./data/data-example/data.parquet")

    # Downloading CSV, JSON, parquet
    download_object(bucket_name, "data.csv", "./data/download/data.csv")
    download_object(bucket_name, "data.json", "./data/download/data.json")
    download_object(bucket_name, "data.parquet", "./data/download/data.parquet")


if __name__ == "__main__":
    main()
