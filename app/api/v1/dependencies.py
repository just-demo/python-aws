from app.config import settings
from app.services.s3_service import S3Service
from app.services.ssm_service import SsmService


# TODO: make a singleton
def get_s3_service() -> S3Service:
    return S3Service(bucket=settings.s3_bucket, endpoint_url=settings.aws_endpoint_url)


def get_ssm_service() -> SsmService:
    return SsmService(endpoint_url=settings.aws_endpoint_url)
