import os
import io
from fastapi import FastAPI, Request
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ConversationHandler, ContextTypes, filters
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
QR, BARCODE = "QR", "BARCODE"
ASK_INPUT = range(1)

app = FastAPI()
application = Application.builder().token(BOT_TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != "private":
        return

    keyboard = [[InlineKeyboardButton("QR", callback_data=QR), InlineKeyboardButton("Barcode", callback_data=BARCODE)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hello, this is Text2Code bot.\n"
        "I can turn your text into a scanable barcode or QR code!\n\n"
        "Please choose what to generate:",
        reply_markup=reply_markup
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != "private":
        return

    await update.message.reply_text(
        "*Text2CodeBot* can instantly turn your text into a scan-able *Barcode* or *QR Code*!\n\n"
        "Type /start to begin.\n\n"
        "*No data is saved — your input is immediately turned into an image and sent back!*\n\n"
        "[GitHub](https://github.com/tal45/text2code)",
        parse_mode="Markdown"
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data["mode"] = query.data
    await query.edit_message_text("Please send the text you want to convert into a " + query.data)
    return ASK_INPUT


async def handle_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    mode = context.user_data.get("mode")

    if mode == QR:
        img = qrcode.make(text)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
    else:
        barcode = Code128(text, writer=ImageWriter())
        buffer = io.BytesIO()
        barcode.write(buffer)

    buffer.seek(0)
    await update.message.reply_photo(photo=buffer)
    return ConversationHandler.END


async def reject(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != "private":
        return
    await update.message.reply_text("Please use /start to begin.")

conv_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(button_handler)],
    states={ASK_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_input)]},
    fallbacks=[]
)

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))
application.add_handler(conv_handler)
application.add_handler(MessageHandler(filters.ALL, reject))


@app.post("/")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, application.bot)
    await application.initialize()
    await application.process_update(update)
    return {"ok": True}
