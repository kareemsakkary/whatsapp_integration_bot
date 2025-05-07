import requests
from integrations import ChatAppIntegration
from models import Message
import os

 
class VonageIntegration(ChatAppIntegration):

    def __init__(self):
        self.api_key = os.getenv("VONAGE_API_KEY")
        self.api_secret = os.getenv("VONAGE_API_SECRET")
        self.whatsapp_number = os.getenv("VONAGE_WHATSAPP_NUMBER")
        self.host_url = os.getenv("HOST_URL")
        self.base_url = "https://messages-sandbox.nexmo.com/v1/messages"

    def return_message(self, message: Message):
        """Send a message using Vonage WhatsApp API."""

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        if message.is_audio:
            # upload audio to Vonage and get the URL
            payload = {
               "from": self.whatsapp_number,
                "to":  message.sender_phone,
                "message_type": "audio",
                "audio": {"url": self.host_url+message.audio_url},
                "channel": "whatsapp",
            }
        else:
            payload = {
                "from": self.whatsapp_number,
                "to":  message.sender_phone,
                "message_type": "text",
                "text": message.body,
                "channel": "whatsapp",
            }

        response = requests.post(
            self.base_url,
            auth=(self.api_key, self.api_secret),
            headers=headers,
            json=payload
        )
        return  response.text, response.status_code

    def receive_message(self, request) -> Message:
        """Parse incoming Vonage message webhook."""
        data = request.get_json()
        message = Message()
        content_type = data.get("message_type", "")
        message.sender_phone = data.get("from", "")
        if content_type == "audio":
            message.is_audio = True
            message.audio_url = data["audio"]["url"]
        elif content_type == "text":
            message.body = data["text"]

        return message
    