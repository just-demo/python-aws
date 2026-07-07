import logging
from fastapi import FastAPI, APIRouter, Request
from starlette.responses import PlainTextResponse

from app.api.v1.router import v1_api_router

logger = logging.getLogger(__name__)

root_router = APIRouter()

app = FastAPI(title="Demo API")


@app.exception_handler(Exception)
def handle_exception(request: Request, error: Exception):
    logger.error(f"Request {request} failed", exc_info=error)
    return PlainTextResponse(status_code=500, content=str(error))


@app.get("/demo")
def demo():
    return "Demo!"


app.include_router(v1_api_router)
logger.info("UP!")
