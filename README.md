# 🤖 Text2Code Bot

[Text2Code Bot](https://t.me/text2code_bot) is a Telegram bot that turns any input string into either a **QR Code** or **Barcode**, and sends it back instantly.  
No storage, no tracking — just fast image generation via inline buttons.

---

## 🚀 Features

- Inline buttons for QR / Barcode choice
- Converts any string into image via BytesIO
- Sends generated image back to user
- Serverless & webhook-powered (Netlify)
- 100% open source and self-hostable

---

## 📦 Project Structure

```
text2code/
├── netlify.toml                  # Netlify config
├── set_webhook.py               # Script to register webhook with Telegram
├── requirements.txt             # Python dependencies
├── .env                         # Contains TELEGRAM_TOKEN and PUBLIC_URL
├── README.md
└── netlify/
    └── functions/
        └── bot.py               # Webhook handler for Telegram
```

---

## 🛠 Local Setup (Dev Mode)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/tal45/text2code.git
   cd text2code
   ```

2. **Create `.env` file**:
   ```env
   TELEGRAM_TOKEN=your-telegram-bot-token
   PUBLIC_URL=https://your-site.netlify.app/webhook
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ☁️ Deploy on Netlify (Free Forever)

1. Push your code to GitHub
2. Go to [Netlify](https://netlify.com) → "Add new site from Git"
3. Pick your repo
4. Set these settings in Netlify:
   - Build command: `pip install -r requirements.txt`
   - Publish directory: (leave empty)
   - Environment variables:
     - `TELEGRAM_TOKEN`: your bot token
     - `PUBLIC_URL`: your netlify url

5. Add this `netlify.toml` in the root:

```toml
[functions]
  node_bundler = "esbuild"

[[redirects]]
  from = "/webhook"
  to = "/.netlify/functions/bot"
  status = 200
```

6. After deploy, run:
   ```bash
   python set_webhook.py
   ```

✅ This registers your bot’s webhook with Telegram.  
From now on, Telegram will send new messages directly to your Netlify function.

---

## 🧪 Testing

- Send `/start` to [@text2code_bot](https://t.me/text2code_bot)
- Use the buttons to generate QR or Barcode
- The image is sent instantly — no data is stored

---

## 📜 License

MIT — use freely, fork it, improve it.
