from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import random
from django.conf import settings
def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp(phone_number, otp):
    # Initialize Twilio client with your Twilio credentials
    client = Client(settings.account_sid, settings.auth_token)

    # Send OTP via SMS using Twilio
    try:
        message = client.messages.create(
            body=f'Your OTP is: {otp}',
            from_='+17867915298',
            to=phone_number
        )
    
        print(f"OTP sent to {phone_number}: {message.sid}")
    except Exception as e:
        print(f"Error sending OTP to {phone_number}: {e}")
    
