# SendPost AWS Lambda Example (Python)

This example demonstrates how to send emails using SendPost in an AWS Lambda function with Python.

## Prerequisites

- AWS Account
- AWS CLI configured
- Python 3.8 or higher
- A SendPost Sub-Account API Key

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt -t .
```

2. Set environment variables in AWS Lambda Console:
- `SENDPOST_API_KEY`: your_sub_account_api_key
- `SENDPOST_FROM_EMAIL`: hello@playwithsendpost.io (optional)
- `SENDPOST_FROM_NAME`: SendPost (optional)

## Deploy

### Using AWS CLI

1. Create deployment package:
```bash
zip -r function.zip lambda_function.py sendpost_python_sdk/ -x "*.pyc" "__pycache__/*"
```

2. Create or update function:
```bash
aws lambda create-function \
  --function-name sendpost-email-python \
  --runtime python3.9 \
  --role arn:aws:iam::YOUR_ACCOUNT:role/lambda-execution-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip \
  --environment Variables="{SENDPOST_API_KEY=your_key}"
```

Or update existing function:
```bash
aws lambda update-function-code \
  --function-name sendpost-email-python \
  --zip-file fileb://function.zip
```

## Test

Invoke the function:
```bash
aws lambda invoke \
  --function-name sendpost-email-python \
  --payload '{"body":"{\"to\":\"recipient@example.com\",\"subject\":\"Test\",\"htmlBody\":\"<h1>Hello</h1>\"}"}' \
  response.json
```

## Notes

- Make sure your sender email domain is verified in your SendPost account
- The function handles both API Gateway events and direct invocations
- Use `var_from` instead of `from` in Python SDK (reserved keyword)
- Environment variables should be set in Lambda configuration, not in code
