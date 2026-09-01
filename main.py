import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv


# ==========================================================
# SETTINGS
# ==========================================================

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# ==========================================================
# BOT
# ==========================================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ==========================================================
# /START
# ==========================================================

@dp.message(CommandStart())
async def start_command(message: Message):

    await message.answer(
        "👋 Hello!\n\n"
        "🤖 Sports News Auto Bot is online!\n"
        "✅ Bot is working correctly."
    )


# ==========================================================
# /HELP
# ==========================================================

@dp.message(Command("help"))
async def help_command(message: Message):

    await message.answer(
        "📖 Available commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/status - Check bot status"
    )


# ==========================================================
# /STATUS
# ==========================================================

@dp.message(Command("status"))
async def status_command(message: Message):

    await message.answer(
        "🟢 Bot Status: ONLINE\n\n"
        "🤖 Sports News Auto Bot\n"
        "⚡ Everything is working."
    )


# ==========================================================
# NORMAL MESSAGE
# ==========================================================

@dp.message()
async def normal_message(message: Message):

    await message.answer(
        "✅ I received your message.\n\n"
        "Use /help to see my commands."
    )


# ==========================================================
# START
# ==========================================================

async def main():

    if not BOT_TOKEN:

        raise RuntimeError(
            "BOT_TOKEN is missing. "
            "Add BOT_TOKEN in Railway Variables."
        )

    me = await bot.get_me()

    logging.info(
        "Bot started successfully: @%s",
        me.username
    )

    await dp.start_polling(bot)


# ==========================================================
# RUN
# ==========================================================

if __name__ == "__main__":
    asyncio.run(main())
