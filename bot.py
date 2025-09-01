from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8459268154:AAEEL88ZEabw1AN7l7ZHJZeh4bSD0JcwyBE"

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Check Balance", callback_data="balance")],
        [InlineKeyboardButton("👥 Referral", callback_data="referral")],
        [InlineKeyboardButton("🎶 Services", callback_data="services")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎵 Welcome to Yuv Music Classes!\nChoose an option below 👇",
        reply_markup=reply_markup
    )

# Callback for buttons
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "balance":
        await query.edit_message_text("💰 Your current balance is: 0 Coins")

    elif query.data == "referral":
        await query.edit_message_text("👥 Invite your friends and earn rewards!\nReferral link: https://t.me/YOUR_BOT?start=ref123")

    elif query.data == "services":
        keyboard = [
            [InlineKeyboardButton("🎸 Guitar Classes", callback_data="guitar")],
            [InlineKeyboardButton("🎤 Western Singing", callback_data="western")],
            [InlineKeyboardButton("🎵 Rock Singing", callback_data="rock")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🎶 Choose a Service:", reply_markup=reply_markup)

    elif query.data in ["guitar", "western", "rock"]:
        contact_text = (
            "📞 Contact Details:\n\n"
            "Tarun Kumar: 7015054260\n"
            "Yuvraj: 7015598966\n"
            "Sumit Verma: 9812121270"
        )
        await query.edit_message_text(contact_text)

# Main function
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
