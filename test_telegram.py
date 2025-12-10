from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8491242969:AAEZDYFAhQntRYBkrgwUjQyfMbvo5ACcKZA"

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message or update.channel_post
    
    if message and message.text:
        chat_type = message.chat.type
        user = message.from_user.username 
        
        print(f"[{chat_type}] {user}: {message.text}")
        
        await message.reply_text(message.text)
        
        print(f"[BOT] {message.text}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()