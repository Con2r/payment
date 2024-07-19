import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

from config import TOKEN, WEBAPP_URL

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# Initialize Bot and Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Open Web App", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    await message.answer(text="Web", reply_markup=markup)

async def main() -> None:
    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
