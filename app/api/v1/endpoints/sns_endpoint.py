import logging

from fastapi import APIRouter, Depends, Body, Response

from app.api.v1.dependencies import get_sns_service
from app.services.sns_service import SnsService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/sns", tags=["sns"])


@router.post("/", status_code=204)
def publish(
        message: str = Body(..., media_type="text/plain"),
        sns_service: SnsService = Depends(get_sns_service),
) -> Response:
    sns_service.publish(message)
    return Response(status_code=204)
