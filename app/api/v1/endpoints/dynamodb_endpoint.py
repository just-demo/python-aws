import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Body, Response

from app.api.v1.dependencies import get_dynamodb_service
from app.models.dynamodb_item import DynamoDbItem
from app.services.dynamodb_service import DynamoDbService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/dynamodb", tags=["dynamodb"])


@router.get("/", response_model=list[DynamoDbItem])
def get_items(
        dynamodb_service: DynamoDbService = Depends(get_dynamodb_service),
) -> list[DynamoDbItem]:
    return dynamodb_service.get_items()


@router.get("/{user_id}/{order_id}", response_model=dict[str, int])
def get_item(
        user_id: str,
        order_id: str,
        dynamodb_service: DynamoDbService = Depends(get_dynamodb_service),
) -> dict[str, int]:
    return dynamodb_service.get_item(user_id, order_id)


@router.put("/{user_id}/{order_id}", status_code=204)
def put_parameter(
        user_id: str,
        order_id: str,
        products: Annotated[dict[str, int], Body()],
        dynamodb_service: DynamoDbService = Depends(get_dynamodb_service),
) -> Response:
    dynamodb_service.put_item(user_id, order_id, products)
    return Response(status_code=204)


@router.delete("/{user_id}/{order_id}", status_code=204)
def delete_object(
        user_id: str,
        order_id: str,
        dynamodb_service: DynamoDbService = Depends(get_dynamodb_service),
) -> Response:
    dynamodb_service.delete_item(user_id, order_id)
    return Response(status_code=204)
