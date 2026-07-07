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
- Environment variables: `PYTHONUNBUFFERED=1;AWS_DEFAULT_REGION=us-east-1;AWS_ACCESS_KEY_ID=dummy;AWS_SECRET_ACCESS_KEY=dummy`
