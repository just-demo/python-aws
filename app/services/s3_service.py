import boto3


class S3Service:
    def __init__(self, bucket: str, endpoint_url: str | None = None):
        self.bucket = bucket
        self.s3_client = boto3.client("s3", endpoint_url=endpoint_url)

    def get_objects(self) -> dict[str, str]:
        keys = [obj["Key"] for obj in self.s3_client.list_objects(Bucket=self.bucket).get("Contents", [])]
        return {key: self.get_object(key) for key in keys}

    def get_object(self, key: str) -> str:
        response = self.s3_client.get_object(
            Bucket=self.bucket,
            Key=key,
        )
        return response["Body"].read().decode("utf-8")

    def put_object(self, key: str, content: str) -> None:
        self.s3_client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=content.encode("utf-8"),
        )

    def delete_object(self, key: str) -> None:
        self.s3_client.delete_object(
            Bucket=self.bucket,
            Key=key,
        )
