#!/usr/bin/env bash

awslocal kinesis create-stream \
  --stream-name demo-kinesis-input-stream-name \
  --shard-count 1 \
  --region us-east-1

awslocal kinesis create-stream \
  --stream-name demo-kinesis-output-stream-name \
  --shard-count 1 \
  --region us-east-1

sleep 5

awslocal kinesis list-streams \
  --region us-east-1