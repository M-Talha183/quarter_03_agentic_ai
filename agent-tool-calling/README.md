
# **WhatsApp Message Sender with Gemini + Twilio**

## 🚀 **Project Overview**

This project is a **WhatsApp messaging agent** that:

- Uses **Google Gemini API (via OpenAI SDK)** to generate friendly WhatsApp messages.
- Sends the generated messages using **Twilio WhatsApp Sandbox**.
- Provides a **Chainlit UI** for easy interaction.

---

## **🛠️ Tech Stack**

| Technology | Purpose |
|------------|---------|
| **Chainlit** | Interactive frontend UI |
| **Google Gemini API** | AI-generated message creation |
| **Twilio WhatsApp API** | Message delivery |
| **Selenium (Optional)** | Previous version used this for WhatsApp Web (Twilio is now used) |
| **Python 3.10+** | Backend logic |

---

## **⚙️ Setup Instructions**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/M-Talha183/quarter_03_agentic_ai.git
cd quarter_03_agentic_ai/agent-tool-calling


### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

### **3️⃣ Configure `.env`**

Create a `.env` file in the root folder:

```bash
GEMINI_API_KEY=your_google_gemini_api_key
ACCOUNT_SID_KEY=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_FROM="your twilio number 
```

---

### **4️⃣ Twilio WhatsApp Sandbox Setup**

- Join the Twilio Sandbox:
    - Send `join thou-voice` to `+14155238886` from your WhatsApp.
- Share the **join code** with friends to allow testing.

---

## **📦 Run the Project**

```bash
chainlit run app.py -w
```

- Open `http://localhost:8000`
- Enter a prompt (e.g., **"Send order confirmation to Noman"**)
- Provide the recipient's WhatsApp number (`+92XXXXXXXXXX`)

---

## **📨 Message Format**

Example user input:

```
Send WhatsApp message:
contact_number: +923********
message: Hello Noman! This is Talha agent. Your order has been confirmed.
```

---

## **🧠 How It Works**

1️⃣ **Gemini API** generates a message based on your prompt.  
2️⃣ **Chainlit UI** asks for the WhatsApp number.  
3️⃣ **Twilio API** sends the message.

---

## **📸 Screenshots**

| Chainlit UI | WhatsApp Output |
|-------------|-----------------|
| ![Chainlit Screenshot](path/to/screenshot1.png) | ![WhatsApp Screenshot](path/to/screenshot2.png) |

---

## **✅ Features**

- 🌍 AI-generated WhatsApp messages
- 🔗 Twilio sandbox integration
- 🖥️ Interactive Chainlit frontend

---

## **🔧 Future Improvements**

- ✅ Add Phonebook Integration  
- ✅ Add Multi-Agent Support (Optional)  
- ✅ Deploy on cloud (e.g., Render / Vercel)

---

## **📄 License**

This project is for educational purposes only.
