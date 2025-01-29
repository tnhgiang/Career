import os
from contextlib import contextmanager
from datetime import datetime
from typing import Union

import pandas as pd
from dagster import IOManager, OutputContext, InputContext
from minio import Minio


@contextmanager
def connect_minio(config):
    client = Minio(
        endpoint=config.get("endpoint_url"),
        access_key=config.get("aws_access_key_id"),
        secret_key=config.get("aws_secret_access_key"),
        secure=False,
    )

    try:
        yield client
    except Exception:
        raise


class MinIOIOManager(IOManager):
    def __init__(self, config):
        self._config = config
        self._create_bucket()

    def _get_path(self, context: Union[InputContext, OutputContext]):
        layer, schema, table = context.asset_key.path
        key = "/".join([layer, schema, table.replace(f"{layer}_", "")])
        tmp_file_path = "/tmp/file-{}-{}.parquet".format(
            datetime.today().strftime("%Y%m%d%H%M%S"),
            "-".join(context.asset_key.path),
        )

        return f"{key}.pq", tmp_file_path

    def _create_bucket(self):
        with connect_minio(self._config) as minio_client:
            bucket = self._config.get("bucket")
            try:
                if not minio_client.bucket_exists(bucket):
                    minio_client.make_bucket(bucket)
            except Exception:
                raise

    def handle_output(self, context: OutputContext, obj: pd.DataFrame):
        # convert to parquet format
        key_name, tmp_file_path = self._get_path(context)
        try:
            # save to pandas file
            obj.to_parquet(tmp_file_path)
            # upload to MinIO
            with connect_minio(self._config) as minio_client:
                minio_client.fput_object(
                    bucket_name=self._config.get("bucket"),
                    object_name=key_name,
                    file_path=tmp_file_path,
                )
            # clean up tmp file
            os.remove(tmp_file_path)
        except Exception:
            raise

    def load_input(self, context: InputContext) -> pd.DataFrame:
        key_name, tmp_file_path = self._get_path(context)
        try:
            # download parquet
            with connect_minio(self._config) as minio_client:
                minio_client.fget_object(
                    bucket_name=self._config.get("bucket"),
                    object_name=key_name,
                    file_path=tmp_file_path,
                )

            # Convert to dataframe
            pd_data = pd.read_parquet(tmp_file_path)

            # clean up tmp file
            os.remove(tmp_file_path)

            return pd_data
        except Exception:
            raise
