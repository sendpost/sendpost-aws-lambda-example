const sendpost = require('sendpost-js-sdk');

const emailApi = new sendpost.EmailApi();
const API_KEY = process.env.SENDPOST_API_KEY;

exports.handler = async (event) => {
  try {
    const { to, subject, htmlBody, textBody } = JSON.parse(event.body || event);
    
    if (!to || !subject || !htmlBody) {
      return {
        statusCode: 400,
        body: JSON.stringify({
          success: false,
          error: 'Missing required fields: to, subject, htmlBody'
        })
      };
    }

    if (!API_KEY) {
      return {
        statusCode: 500,
        body: JSON.stringify({
          success: false,
          error: 'SENDPOST_API_KEY not configured'
        })
      };
    }
    
    const emailMessage = new sendpost.EmailMessage();
    emailMessage.from = {
      email: process.env.SENDPOST_FROM_EMAIL || 'hello@playwithsendpost.io',
      name: process.env.SENDPOST_FROM_NAME || 'SendPost'
    };
    emailMessage.to = [{ email: to }];
    emailMessage.subject = subject;
    emailMessage.htmlBody = htmlBody;
    emailMessage.textBody = textBody || htmlBody.replace(/<[^>]*>/g, '');
    emailMessage.trackOpens = true;
    emailMessage.trackClicks = true;

    const response = await emailApi.sendEmail(API_KEY, { emailMessage });

    return {
      statusCode: 200,
      body: JSON.stringify({
        success: true,
        messageId: response.messageId
      })
    };
  } catch (error) {
    console.error('SendPost error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({
        success: false,
        error: error.message
      })
    };
  }
};
