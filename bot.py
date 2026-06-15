from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    welcome_text = """
🔞 PREMIUM ACCESS PREVIEW

The images below are sample previews only.

🔥 Premium Membership Includes:

✅ Lifetime Access
✅ Exclusive Viral Collections
✅ Instagram Viral Content Library
✅ Daily Content Updates
✅ Premium Packs & Archives
✅ Private Members-Only Group
✅ New Content Added Regularly
✅ Instant Access After Verification

📌 These previews represent only a small portion of the premium collection.

💎 Want Full Access?

DM NOW:
👉 @universe

After payment confirmation, you will be added to the premium group and receive lifetime access to all current and future updates.

⚠️ Strictly for Adults (18+) Only.
"""

    await update.message.reply_text(welcome_text)

    for file in sorted(os.listdir("images")):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
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

