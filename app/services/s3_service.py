import boto3


class S3Service:
    def __init__(self, bucket: str, endpoint_url=None):
        self.bucket = bucket
        self.s3_client = boto3.client("s3", endpoint_url=endpoint_url)

    def put_object(self, key: str, content: str) -> None:
        self.s3_client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=content.encode("utf-8"),
        )

    def get_object(self, key: str) -> str:
        response = self.s3_client.get_object(
            Bucket=self.bucket,
            Key=key,
        )
        return response["Body"].read().decode("utf-8")

    def delete_object(self, key: str) -> None:
        self.s3_client.delete_object(
            Bucket=self.bucket,
            Key=key,
        )
