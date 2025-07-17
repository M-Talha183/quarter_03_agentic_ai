# Assignment WhatsApp Tool 🤖📲

**Assignment WhatsApp Tool** is an AI-powered WhatsApp messaging agent built in **Python** using **Chainlit**, **Gemini LLM API**, and the **OpenAI SDK (AsyncOpenAI)**.  
This tool simulates a **"Rishtay Wali Auntie"** that matches users based on age and sends WhatsApp messages directly via the **UltraMSG API**.

---

## 📂 **Repository Info**

📦 **GitHub Repository:**  
https://github.com/M-Talha183/quarter_03_agentic_ai

📁 **Project Folder:**  
`assignment-whatsapp-tool`

---

## 🚀 **Features**

- 🤖 **Rishtay Wali Auntie Agent**  
  Matches users based on a minimum age filter.

- 📲 **WhatsApp Integration**  
  Sends WhatsApp messages using **UltraMSG API**.

- 🧰 **Custom Function Tools**  
  Uses `function_tool` decorators for real-world functions (data filtering + messaging).

- 💾 **Session Management**  
  Maintains user history in sessions with **Chainlit**.

---

## 🛠️ **Technologies Used**

- **Python 3.10+**
- **Chainlit**
- **AsyncOpenAI SDK (with Gemini LLM API)**
- **UltraMSG API (for WhatsApp messaging)**
- **dotenv (for environment variables)**

---

## ⚙️ **Setup & Installation**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/M-Talha183/quarter_03_agentic_ai.git
cd quarter_03_agentic_ai/assignment-whatsapp-tool

Install Dependencies
Using uv (recommended):

uv pip install -r requirements.txt

Environment Variables
Create a .env file inside assignment-whatsapp-tool/:

GEMINI_API_KEY=your_gemini_api_key
INSTANCE_ID=your_ultramsg_instance_id
TOKEN=your_ultramsg_api_token

/

💻 How to Run

cd assignment-whatsapp-tool

# Run the Chainlit app
chainlit run main.py

Project Structure
quarter_03_agentic_ai/
│
├── assignment-whatsapp-tool/
│   ├── main.py                # Main logic (AI agent + Chainlit)
│   ├── whatsapp.py            # WhatsApp message sending function
│   ├── .env                    # API keys and tokens
│   └── requirements.txt        # Python dependencies
│
└── other projects ...
UltraMSG API
API Docs: https://ultramsg.com/

Supports sending WhatsApp messages without requiring WhatsApp Web.


