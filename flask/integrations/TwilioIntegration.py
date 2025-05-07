from twilio.twiml.messaging_response import MessagingResponse
from integrations import ChatAppIntegration
from models.message import Message


 
class TwilioIntegration(ChatAppIntegration):

    def return_message(self, message: Message):
        """Send a message using Twilio."""
        resp = MessagingResponse()

        if message.is_audio:
            resp_message = resp.message("respond")
            resp_message.media(message.audio_url)
        else:
            resp.message(message.body)
        return str(resp)

    def receive_message(self, request) -> Message:
        """Receive a message using Twilio."""
        media_type = request.values.get('MediaContentType0', '')
        message = Message()
        if media_type == "audio/ogg":
            message.is_audio = True
            message.audio_url = request.values.get('MediaUrl0')
            return message
        else:
            message.body = request.values.get('Body', '')
            message.sender_phone = request.values.get('From', '')
            return message
