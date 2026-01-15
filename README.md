# SendPost AWS Lambda Examples

This repository contains examples for using SendPost with AWS Lambda in different runtimes.

## Examples

- [Node.js](./nodejs/) - JavaScript Lambda function
- [Python](./python/) - Python Lambda function

## Common Setup

1. Get your SendPost Sub-Account API Key from [SendPost Dashboard](https://app.sendpost.io)
2. Set environment variables in AWS Lambda Console:
   - `SENDPOST_API_KEY`: your_sub_account_api_key
   - `SENDPOST_FROM_EMAIL`: hello@playwithsendpost.io (optional)
   - `SENDPOST_FROM_NAME`: SendPost (optional)

## Deployment

See the README in each subdirectory for specific deployment instructions.

## Notes

- Make sure your sender email domain is verified in your SendPost account
- Environment variables should be set in Lambda configuration
- The functions handle both API Gateway events and direct invocations
