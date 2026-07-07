import boto3


class SsmService:
    def __init__(self, endpoint_url: str | None = None):
        self.client = boto3.client(
            "ssm",
            endpoint_url=endpoint_url,
        )

    def get_parameters(self) -> dict[str, str]:
        paginator = self.client.get_paginator("describe_parameters")
        names = [param["Name"] for page in paginator.paginate() for param in page["Parameters"]]
        return {name: self.get_parameter(name) for name in names}

    def get_parameter(self, name: str) -> str:
        response = self.client.get_parameter(
            Name=name,
            WithDecryption=True,
        )
        return response["Parameter"]["Value"]

    def put_parameter(self, name: str, value: str) -> None:
        self.client.put_parameter(
            Name=name,
            Value=value,
            Type="SecureString",
            Overwrite=True,
        )

    def delete_parameter(self, name: str) -> None:
        self.client.delete_parameter(
            Name=name,
        )
