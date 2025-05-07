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

# A simple in-memory structure to store tasks
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        message = twilioIntegration.receive_message(request)
        answer = bot.run(message)
    except Exception as e:
        answer = Message()
        answer.body = f"{e}"
    response = twilioIntegration.return_message(answer)
    return str(response)

# A simple in-memory structure to store tasks
@app.route('/webhook-vonage', methods=['POST'])
def webhook_vonage():
    try:
        message = vonageIntegration.receive_message(request)
        print(message.body)
        answer = bot.run(message)
    except Exception as e:
        answer = Message()
        answer.body = f"{e}"
    response = vonageIntegration.return_message(answer)
    return str(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
