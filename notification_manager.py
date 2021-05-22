from twilio.rest import Client
from decouple import config

TWILIO_SID = config("TWILIO_SID", default="")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN", default="")
TWILIO_VIRTUAL_NUMBER = config("TWILIO_VIRTUAL_NUMBER", default="")
TWILIO_VERIFIED_NUMBER = config("TWILIO_VERIFIED_NUMBER", default="")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)
