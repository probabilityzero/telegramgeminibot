import os
import time
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

history = {}
last_call = {}
DELAY = 1.2


def sender(u):
    return f"{u.username}" if u.username else str(u.id)


def build_history(cid, user_text):
    if cid not in history:
        history[cid] = [
            {"role": "system", "content": "You are Damian's assistant, your name is Herald, you speak in simple victorian English."}
        ]
    history[cid].append({"role": "user", "content": user_text})
    history[cid] = history[cid][-16:]


def get_reply(cid):
    resp = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=history[cid],
        temperature=0.7,
    )
    return resp.choices[0].message.content


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message
    if not m or not m.text:
        return

    cid = m.chat.id
    text = m.text
    user = sender(m.from_user)

    print(f"[{cid}] {user}: {text}")

    now = time.time()
    if now - last_call.get(cid, 0) < DELAY:
        print("[RATE-LIMIT] Please wait before sending another message.")
        return
    last_call[cid] = now

    build_history(cid, text)

    try:
        reply = get_reply(cid)
    except Exception as e:
        reply = f"[AI ERROR] {e}"

    print("[AI]:", reply)

    await context.bot.send_message(chat_id=cid, text=reply)


def main():
    app = ApplicationBuilder().token(os.getenv("GROQ_TELEGRAM_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("Bot is running with GROQ LLM...")
    app.run_polling()


if __name__ == "__main__":
    main()