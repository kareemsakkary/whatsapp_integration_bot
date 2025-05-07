# WhatsApp Chatbot for Equation Evaluation

## 📋 Overview

This project is a WhatsApp-integrated chatbot that evaluates mathematical expressions sent by users. It also handles voice messages by replying with a pre-recorded prompt asking the user to resubmit their query as text.

The system is built with scalability and modularity in mind, allowing future extensions such as AI-based bots, customer service tools, and integration with various WhatsApp Business APIs.

---

## 🎯 Objectives

- Integrate a chatbot with WhatsApp using APIs like **Twilio** and **Vonage**
- Parse and evaluate mathematical expressions sent as text
- Handle unsupported message types (e.g., voice notes) with automated responses
- Ensure secure and efficient error handling
- Develop a scalable backend that can integrate with other platforms and bot types

---

## 🛠️ Technologies Used

- **Python**: Core language for backend logic and message processing
- **Flask**: Lightweight web framework for RESTful API endpoints
- **Twilio & Vonage APIs**: To send and receive WhatsApp messages
- **Defang**: Platform used for reliable backend deployment
- **Postman & Ngrok**: For local testing and webhook simulation

---

## 🧠 System Architecture

> *(Diagram not included – you can insert a diagram here if you have one)*

---

## ▶️ How to Use

The bot is available on two WhatsApp sandbox environments:

### Method 1: Using Twilio Sandbox
1. Save the number **+1 (415) 523-8886** and open a WhatsApp chat with it.
2. Send the message: `Join tent-bowl` to activate the Twilio sandbox.

### Method 2: Using Vonage Sandbox
1. Save the number **+1 (415) 738-6102** and open a WhatsApp chat with it.
2. Send the message: `Join crush taste` to activate the Vonage sandbox.

### Interaction
Once the session is active:
- ✅ Send a math expression like `12 / (3 + 1)` — you'll receive the evaluated result.
- 🎤 Send a voice note — the bot will reply with a voice prompt asking for a text-based query.

---

## ✨ Features

### ✅ Modular Design
- Backend separates core logic from provider-specific logic
- Easily extendable to other WhatsApp providers or bot types

### ✅ Text Message Handling
- Uses regex to extract valid math expressions from mixed text
- Securely evaluates and responds with results via WhatsApp

### ✅ Voice Message Handling
- Detects incoming voice notes
- Sends a pre-recorded message prompting for text input

---

## 🔁 Service Flow

1. **Webhook Triggered**: `/webhook-twilio` or `/webhook-vonage` receives a message
2. **Parsing**: Message is converted into a unified `Message` object
3. **Processing**: 
    - Math expression is extracted and evaluated
    - Response message is built
4. **Response**: Sent back to the user via the respective API (Twilio or Vonage)

---

## 🧩 Challenges & Solutions

### 🚫 Twilio Daily Message Limit
- Twilio sandbox allows only a limited number of trial messages per day

### ✅ Workaround
- Added **Vonage** as an alternative provider
- Created new Twilio trial accounts to bypass message limits during testing

---

## 🔮 Future Improvements

- ✅ Deploy with a **dedicated WhatsApp number** (not using sandbox join codes)
- 🔌 Extend functionality to support:
  - AI-based bots
  - Internal business tools
  - Customer support automation

