# 🤖 Text2Code Bot

[Text2Code Bot](https://t.me/text2code_bot) is a Telegram bot that turns any input string into a **QR Code** or **Barcode**, and sends it back instantly — no storage, no polling, just lightweight webhook-powered magic.

---

## 🚀 Features

- Inline buttons for QR / Barcode selection
- Converts text into an image using BytesIO
- Hosted serverlessly with **Render** + **FastAPI**
- No user data is saved
- 100% open-source and free to use

---

## 🧱 Project Structure

```
.
├── main.py               # FastAPI app + Telegram logic
├── requirements.txt      # Minimal dependency list
├── set_webhook.py        # Register your webhook with Telegram
├── .env                  # Bot token and public URL
└── render.yaml           # Deployment config for Render
```

---

## 🛠 Local Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/tal45/text2code.git
   cd text2code
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**:
   ```env
   TELEGRAM_TOKEN=your-telegram-bot-token
   PUBLIC_URL=https://your-app.onrender.com
   ```

---

## ☁️ Deployment on Render

1. Push to GitHub
2. Create a **new Render Web Service**
3. Set:
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
   - **Environment variable**: `TELEGRAM_TOKEN=your-bot-token`
4. Deploy!

---

## 🔗 Register Your Webhook

Once deployed, tell Telegram where to send updates:

```bash
python set_webhook.py
```

> Make sure your `.env` contains `PUBLIC_URL=https://your-app.onrender.com`

---

## ✅ Example Flow

1. User sends `/start`
2. Bot shows buttons: `QR` / `Barcode`
3. User selects a mode and sends text
4. Bot sends back a generated image
5. 🎉 Done!

---

## 📜 License

MIT — use freely, improve it, ship it.
