from fastapi import APIRouter
from app.api.v1.endpoints.demo_s3 import router as s3_router

v1_api_router = APIRouter()

v1_api_router.include_router(s3_router)
