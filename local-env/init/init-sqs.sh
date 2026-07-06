#!/usr/bin/env bash

awslocal sqs create-queue \
  --queue-name demo-sqs-queue-name.fifo \
  --attributes VisibilityTimeout=2,FifoQueue=true \
  --region us-east-1