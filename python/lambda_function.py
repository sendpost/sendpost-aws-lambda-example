import os
import json
import sendpost_python_sdk
from sendpost_python_sdk.api import EmailApi
from sendpost_python_sdk.models import EmailMessageObject, EmailAddress, Recipient

def lambda_handler(event, context):
    try:
        # Parse request body
        if isinstance(event.get('body'), str):
            body = json.loads(event['body'])
        else:
            body = event.get('body', event)
        
        to = body.get('to')
        subject = body.get('subject')
        html_body = body.get('htmlBody')
        
        if not all([to, subject, html_body]):
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'success': False,
                    'error': 'Missing required fields: to, subject, htmlBody'
                })
            }
        
        api_key = os.getenv('SENDPOST_API_KEY')
        if not api_key:
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'success': False,
                    'error': 'SENDPOST_API_KEY not configured'
                })
            }
        
        # Configure SendPost
        configuration = sendpost_python_sdk.Configuration(
            host="https://api.sendpost.io/api/v1"
        )
        configuration.api_key['subAccountAuth'] = api_key
        
        with sendpost_python_sdk.ApiClient(configuration) as api_client:
            email_message = EmailMessageObject()
            email_message.var_from = EmailAddress(
                email=os.getenv('SENDPOST_FROM_EMAIL', 'hello@playwithsendpost.io'),
                name=os.getenv('SENDPOST_FROM_NAME', 'SendPost')
            )
            email_message.to = [Recipient(email=to)]
            email_message.subject = subject
            email_message.html_body = html_body
            
            response = EmailApi(api_client).send_email(email_message)[0]
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'success': True,
                    'messageId': response.message_id
                })
            }
    except sendpost_python_sdk.exceptions.ApiException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'success': False,
                'error': f"API Error {e.status}: {e.body}"
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'success': False,
                'error': str(e)
            })
        }
