from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    aws_endpoint_url: str | None = None
    s3_bucket: str
    dynamodb_table_name: str

    model_config = SettingsConfigDict(
        env_file="demo.env",
        env_prefix="DEMO_",
    )


settings = Settings()
