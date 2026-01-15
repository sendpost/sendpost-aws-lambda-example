# SendPost AWS Lambda Example (Node.js)

This example demonstrates how to send emails using SendPost in an AWS Lambda function with Node.js.

## Prerequisites

- AWS Account
- AWS CLI configured
- Node.js 14 or higher
- A SendPost Sub-Account API Key

## Setup

1. Install dependencies:
```bash
npm install
```

2. Set environment variables in AWS Lambda Console:
- `SENDPOST_API_KEY`: your_sub_account_api_key
- `SENDPOST_FROM_EMAIL`: hello@playwithsendpost.io (optional)
- `SENDPOST_FROM_NAME`: SendPost (optional)

## Deploy

### Using AWS CLI

1. Create deployment package:
```bash
zip -r function.zip index.js node_modules package.json
```

2. Create or update function:
```bash
aws lambda create-function \
  --function-name sendpost-email \
  --runtime nodejs18.x \
  --role arn:aws:iam::YOUR_ACCOUNT:role/lambda-execution-role \
  --handler index.handler \
  --zip-file fileb://function.zip \
  --environment Variables="{SENDPOST_API_KEY=your_key}"
```

Or update existing function:
```bash
aws lambda update-function-code \
  --function-name sendpost-email \
  --zip-file fileb://function.zip
```

### Using Serverless Framework

Create `serverless.yml`:
```yaml
service: sendpost-email

provider:
  name: aws
  runtime: nodejs18.x
  environment:
    SENDPOST_API_KEY: ${env:SENDPOST_API_KEY}

functions:
  sendEmail:
    handler: index.handler
    events:
      - http:
          path: send-email
          method: post
```

Deploy:
```bash
serverless deploy
```

## Test

Invoke the function:
```bash
aws lambda invoke \
  --function-name sendpost-email \
  --payload '{"body":"{\"to\":\"recipient@example.com\",\"subject\":\"Test\",\"htmlBody\":\"<h1>Hello</h1>\"}"}' \
  response.json
```

## Notes

- Make sure your sender email domain is verified in your SendPost account
- The function handles both API Gateway events and direct invocations
- Environment variables should be set in Lambda configuration, not in code
