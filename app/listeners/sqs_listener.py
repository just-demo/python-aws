import logging
import threading
from contextlib import asynccontextmanager
import boto3
from fastapi import FastAPI

from app.config import settings

logger = logging.getLogger(__name__)

sqs_client = boto3.client("sqs", endpoint_url=settings.aws_endpoint_url)
stop_event = threading.Event()


def listen():
    while not stop_event.is_set():
        try:
            response = sqs_client.receive_message(
                QueueUrl=settings.sqs_queue_url,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=20,
            )

            logger.info(f"SQS response received: {response}")
            for message in response.get("Messages", []):
                logger.info(f"SQS message received: {message["Body"]}")

                sqs_client.delete_message(
                    QueueUrl=settings.sqs_queue_url,
                    ReceiptHandle=message["ReceiptHandle"],
                )

        except Exception:
            logger.exception("SQS listener failed")


@asynccontextmanager
async def lifespan(app: FastAPI):
    thread = threading.Thread(target=listen, daemon=True)
    thread.start()

    try:
        yield
    finally:
        stop_event.set()
        thread.join(timeout=25)
