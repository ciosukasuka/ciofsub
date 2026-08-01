import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, CHANNEL_ID, LOG_CHANNEL, ADMINS

Bot = Client(
    "fsub_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=300
)

@Bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply(
        f"Halo {message.from_user.first_name}!\nBot Fsub sudah jalan ✅"
    )

async def main():
    await Bot.start()
    # Test kirim ke log channel biar tau bot hidup
    try:
        await Bot.send_message(LOG_CHANNEL, "Bot: Fsub Started successfully ✅")
    except Exception as e:
        print(f"Gagal kirim ke LOG_CHANNEL: {e}")

    print("Bot Started")
    await idle()
    await Bot.stop()

from pyrogram import idle
Bot.run(main())
