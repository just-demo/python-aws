import logging

from fastapi import APIRouter, Depends, Body, Response
from fastapi.responses import PlainTextResponse

from app.dependencies import get_s3_service
from app.services.s3_service import S3Service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/s3", tags=["s3"])


@router.get("/", response_model=dict[str, str])
def get_objects(
        s3_service: S3Service = Depends(get_s3_service),
) -> dict[str, str]:
    return s3_service.get_objects()


@router.get("/{key}", response_class=PlainTextResponse)
def get_object(
        key: str,
        s3_service: S3Service = Depends(get_s3_service),
) -> str:
    return s3_service.get_object(key)


@router.put("/{key}", status_code=204)
def put_object(
        key: str,
        value: str = Body(..., media_type="text/plain"),
        s3_service: S3Service = Depends(get_s3_service),
) -> Response:
    s3_service.put_object(key, value)
    return Response(status_code=204)


@router.delete("/{key}", status_code=204)
def delete_object(
        key: str,
        s3_service: S3Service = Depends(get_s3_service),
) -> Response:
    s3_service.delete_object(key)
    return Response(status_code=204)
