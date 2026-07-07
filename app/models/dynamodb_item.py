from pydantic import BaseModel, Field


class DynamoDbItem(BaseModel):
    userId: str
    orderId: str
    products: dict[str, int] = Field(default_factory=dict)