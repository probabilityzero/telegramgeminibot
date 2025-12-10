from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8491242969:AAEZDYFAhQntRYBkrgwUjQyfMbvo5ACcKZA"

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.business_message:
        message = update.business_message
        chat_type = message.chat.type
        user = message.from_user.username if message.from_user else "Unknown"
        
        print(f"[business-{chat_type}] {user}: {message.text}")
        
        await context.bot.send_message(
            business_connection_id=message.business_connection_id,
            chat_id=message.chat.id,
            text=message.text
        )
        
        print(f"[BOT] Echoed: {message.text}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Bot started...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()