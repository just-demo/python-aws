import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

from app.models.dynamodb_item import DynamoDbItem


class DynamoDbService:
    def __init__(self, table_name: str, endpoint_url: str | None = None):
        self.table_name = table_name
        self.client = boto3.client("dynamodb", endpoint_url=endpoint_url)
        self.serializer = TypeSerializer()
        self.deserializer = TypeDeserializer()

    def get_items(self) -> list[DynamoDbItem]:
        response = self.client.scan(TableName=self.table_name)
        return [
            DynamoDbItem.model_validate({
                k: self.deserializer.deserialize(v)
                for k, v in item.items()
            })
            for item in response.get("Items", [])
        ]

    def get_item(
            self,
            user_id: str,
            order_id: str,
    ) -> dict[str, int] | None:
        response = self.client.get_item(
            TableName=self.table_name,
            Key={
                "userId": self.serializer.serialize(user_id),
                "orderId": self.serializer.serialize(order_id),
            },
        )

        products = response.get("Item", {}).get("products")
        return {} if products is None else self.deserializer.deserialize(products)

    def put_item(
            self,
            user_id: str,
            order_id: str,
            products: dict[str, int],
    ) -> None:
        self.client.put_item(
            TableName=self.table_name,
            Item={
                "userId": self.serializer.serialize(user_id),
                "orderId": self.serializer.serialize(order_id),
                "products": self.serializer.serialize(products),
            },
        )

    def delete_item(
            self,
            user_id: str,
            order_id: str,
    ) -> None:
        self.client.delete_item(
            TableName=self.table_name,
            Key={
                "userId": self.serializer.serialize(user_id),
                "orderId": self.serializer.serialize(order_id),
            },
        )
