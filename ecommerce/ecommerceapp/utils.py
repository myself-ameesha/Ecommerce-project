from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import random

def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp(phone_number, otp):
    # Initialize Twilio client with your Twilio credentials
    account_sid = "ACc9ccfade44a44e8dfd940caca0058b27"
    auth_token = "9e0ff7204247cbb8ca8b671046b26910"
    client = Client(account_sid, auth_token)

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
    