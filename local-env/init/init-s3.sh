#!/usr/bin/env bash

awslocal s3 mb s3://demo-s3-bucket \
  --region us-east-1

awslocal s3 ls \
  --region us-east-1
