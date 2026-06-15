from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio


TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome!")

    for file in os.listdir("images"):
        if file.endswith((".jpg", ".jpeg", ".png")):
            with open(os.path.join("images", file), "rb") as img:
                await update.message.reply_photo(img)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

async def main():
    print("Bot is running...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
