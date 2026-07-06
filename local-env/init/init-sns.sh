#!/usr/bin/env bash

awslocal sns create-topic \
  --name demo-sns-topic-name \
  --region us-east-1

awslocal sqs create-queue \
  --queue-name demo-sns-topic-name-verifier \
  --region us-east-1

awslocal sns subscribe --protocol sqs \
  --topic-arn arn:aws:sns:us-east-1:000000000000:demo-sns-topic-name \
  --notification-endpoint arn:aws:sqs:us-east-1:000000000000:demo-sns-topic-name-verifier \
  --region us-east-1
