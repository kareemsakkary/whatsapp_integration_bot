from flask import Flask, jsonify, request, render_template_string
from integrations import TwilioIntegration
from integrations import VonageIntegration
from bots import MathmaticalBot
from models import Message
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


twilioIntegration = TwilioIntegration()
vonageIntegration = VonageIntegration()
bot = MathmaticalBot()


@app.route('/')
def index():
    return render_template_string("""
    <html>
        <head><title>Chatbot</title></head>
        <body>
            <h1>Chatbot</h1>
            <p>Send a message to the bot.</p>
        </body>
    </html>
    """)

@app.route('/webhook-twilio', methods=['POST'])
def webhook():
    return recive_message(twilioIntegration, request)
 
@app.route('/webhook-vonage', methods=['POST'])
def webhook_vonage():
    return recive_message(vonageIntegration, request)\
    

def recive_message(chat_app_integration, request):
    """Run the chat app integration."""
    message = chat_app_integration.receive_message(request)
    if message.body == "" or message.sender_phone == "":
        return jsonify({"error": "Invalid message"}), 400
    try:
        answer = bot.run(message)
        response = chat_app_integration.return_message(answer)
    except Exception as e:
        answer = Message()
        answer.body = f"{e}"
        answer.sender_phone = message.sender_phone
        response = chat_app_integration.return_message(answer)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
