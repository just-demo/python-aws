from functools import lru_cache
from app.config import settings
from app.services.dynamodb_service import DynamoDbService
from app.services.s3_service import S3Service
from app.services.sns_service import SnsService
from app.services.ssm_service import SsmService


@lru_cache
def get_s3_service() -> S3Service:
    return S3Service(bucket=settings.s3_bucket, endpoint_url=settings.aws_endpoint_url)


@lru_cache
def get_ssm_service() -> SsmService:
    return SsmService(endpoint_url=settings.aws_endpoint_url)


@lru_cache
def get_dynamodb_service() -> DynamoDbService:
    return DynamoDbService(table_name=settings.dynamodb_table_name, endpoint_url=settings.aws_endpoint_url)


@lru_cache
def get_sns_service() -> SnsService:
    return SnsService(topic_arn=settings.sns_topic_arn, endpoint_url=settings.aws_endpoint_url)
