# sms_service.py

import africastalking
from django.conf import settings

# Initialize the SDK
username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY

africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS

def send_sms(recipients, message):
    try:
        response = sms.send(message, recipients)
        return response
    except Exception as e:
        print(f'Encountered an error while sending: {e}')
        return {'status': 'error', 'message': str(e)}
