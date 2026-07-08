import boto3


class SnsService:
    def __init__(self, topic_arn: str, endpoint_url: str | None = None):
        self.topic_arn = topic_arn
        self.sns_client = boto3.client("sns", endpoint_url=endpoint_url)

    def publish(self, message: str) -> None:
        self.sns_client.publish(
            TopicArn=self.topic_arn,
            Message=message,
            Subject="UserCreated",
        )
