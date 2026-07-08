# Python AWS

## Swagger

http://localhost:8000/docs

## Prepare Python virtual environment

```
brew install pyenv
pyenv install 3.14.3
$(pyenv root)/versions/3.14.3/bin/python -m venv .venv
source .venv/bin/activate
```

## Init dependencies

```
pip install pip-tools
pip-compile --upgrade -o requirements.txt requirements.in
pip-compile --upgrade -o requirements-test.txt requirements-test.in
```

## Install dependencies

```
pip install -r requirements.txt
pip install -r requirements-test.txt
```

## Run local env to mock AWS services:

```
docker compose -f local-env/docker-compose.yaml up --force-recreate
```

## Run from IDE

- Script path: `<full/path/to>/python-aws/.venv/bin/uvicorn`
- Parameters: `app.main:app --reload`
- Working directory: `<full/path/to>/python-aws`
- Environment variables:
  `PYTHONUNBUFFERED=1;AWS_DEFAULT_REGION=us-east-1;AWS_ACCESS_KEY_ID=dummy;AWS_SECRET_ACCESS_KEY=dummy`

## Test S3

```
aws s3api put-object \
  --endpoint-url=http://localhost:4566 \
  --bucket demo-s3-bucket \
  --key just-demo \
  --body <path/to/local/file> \
  --region us-east-1
```

## Test Kinesis:

```
aws kinesis put-record \
  --endpoint-url=http://localhost:4566 \
  --region us-east-1 \
  --stream-name demo-kinesis-input-stream-name \
  --partition-key dummy \
  --cli-binary-format raw-in-base64-out \
  --data '{"user_id": "123", "order_id": "456"}'
```

or

```
aws kinesis put-record \
  --endpoint-url=http://localhost:4566 \
  --region us-east-1 \
  --stream-name demo-kinesis-input-stream-name \
  --partition-key dummy \
  --cli-binary-format raw-in-base64-out \
  --data file://just-demo.json
```

## Test SQS

Send a message:

```
aws sqs send-message \
  --message-body "Just Demo" \
  --message-group-id "group-1" \
  --message-deduplication-id "$(uuidgen)" \
  --queue-url http://localhost:4566/000000000000/demo-sqs-queue-name.fifo \
  --endpoint-url=http://localhost:4566 \
  --region us-east-1
```

Verify no messages left:

````
aws sqs receive-message \
  --endpoint-url=http://localhost:4566 \
  --queue-url http://localhost:4566/000000000000/demo-sqs-queue-name.fifo \
  --region us-east-1
````

## Test SNS

Trigger publishing with API and then verify:

````
aws sqs receive-message \
  --endpoint-url=http://localhost:4566 \
  --queue-url http://localhost:4566/000000000000/demo-sns-topic-name-verifier \
  --region us-east-1
````

## Docker Deployment

```
docker build -t python-aws .
docker run \
  --network local-env_default \
  -p 8000:8000 \
  -e AWS_DEFAULT_REGION=us-east-1 \
  -e AWS_ACCESS_KEY_ID=dummy \
  -e AWS_SECRET_ACCESS_KEY=dummy \
  -e DEMO_AWS_ENDPOINT_URL=http://localstack:4566 \
  -e DEMO_SQS_QUEUE_URL=http://localstack:4566/000000000000/demo-sqs-queue-name.fifo \
  python-aws
```