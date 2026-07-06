#!/usr/bin/env bash

awslocal dynamodb create-table \
  --table-name demo-dynamodb-table-name \
  --attribute-definitions \
      AttributeName=userId,AttributeType=S \
      AttributeName=orderId,AttributeType=S \
  --key-schema \
      AttributeName=userId,KeyType=HASH \
      AttributeName=orderId,KeyType=RANGE \
  --provisioned-throughput \
      ReadCapacityUnits=5,WriteCapacityUnits=5 \
  --region us-east-1
