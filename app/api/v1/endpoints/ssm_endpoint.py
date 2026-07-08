import logging

from fastapi import APIRouter, Depends, Body, Response
from fastapi.responses import PlainTextResponse

from app.dependencies import get_ssm_service
from app.services.ssm_service import SsmService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/ssm", tags=["ssm"])


@router.get("/", response_model=dict[str, str])
def get_parameters(
        ssm_service: SsmService = Depends(get_ssm_service),
) -> dict[str, str]:
    return ssm_service.get_parameters()


@router.get("/{name}", response_class=PlainTextResponse)
def get_object(
        name: str,
        ssm_service: SsmService = Depends(get_ssm_service),
) -> str:
    return ssm_service.get_parameter(name)


@router.put("/{name}", status_code=204)
def put_parameter(
        name: str,
        value: str = Body(..., media_type="text/plain"),
        ssm_service: SsmService = Depends(get_ssm_service),
) -> Response:
    ssm_service.put_parameter(name, value)
    return Response(status_code=204)


@router.delete("/{name}", status_code=204)
def delete_object(
        name: str,
        ssm_service: SsmService = Depends(get_ssm_service),
) -> Response:
    ssm_service.delete_parameter(name)
    return Response(status_code=204)
