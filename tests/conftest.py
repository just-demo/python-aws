import os

import boto3
import pytest
from fastapi.testclient import TestClient
from testcontainers.localstack import LocalStackContainer

from app.main import app
from app.dependencies import get_s3_service
from app.services.s3_service import S3Service

BUCKET_NAME = "test-bucket"


@pytest.fixture(scope="session")
def localstack():
    with LocalStackContainer(image="localstack/localstack:4.14") as ls:
        endpoint_url = ls.get_url()

        os.environ["AWS_ACCESS_KEY_ID"] = "test"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
        os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

        s3_client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            region_name="us-east-1",
        )

        s3_client.create_bucket(Bucket=BUCKET_NAME)

        yield {
            "endpoint_url": endpoint_url,
            "s3_bucket": BUCKET_NAME,
            "s3_client": s3_client,
        }


@pytest.fixture()
def rest_client(localstack):
    s3_service = S3Service(
        bucket=localstack["s3_bucket"],
        endpoint_url=localstack["endpoint_url"],
    )

    app.dependency_overrides[get_s3_service] = lambda: s3_service

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
