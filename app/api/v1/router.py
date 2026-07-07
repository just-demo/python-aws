from fastapi import APIRouter
from app.api.v1.endpoints.s3_endpoint import router as s3_router
from app.api.v1.endpoints.ssm_endpoint import router as ssm_router
from app.api.v1.endpoints.dynamodb_endpoint import router as dynamodb_router

v1_api_router = APIRouter()

v1_api_router.include_router(s3_router)
v1_api_router.include_router(ssm_router)
v1_api_router.include_router(dynamodb_router)
