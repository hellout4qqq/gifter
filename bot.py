import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# ⚠️ СЮДА ВСТАВЬТЕ ТОКЕН ИЗ @BotFather (внутри кавычек)
BOT_TOKEN = "8957601323:AAHa1SJpfUt_h16NxQd36yOY2gvRrDEyzPU"

# Ваша готовая ссылка на игру
WEB_APP_URL = "https://github.io" 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎮 Играть в Gift Battle",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])
    
    welcome_text = (
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Добро пожаловать в симулятор визуальных NFT-подарков **Gift Battle**!\n"
        "Жми кнопку ниже, чтобы начать игру прямо внутри Telegram 👇"
    )
    await message.answer(welcome_text, reply_markup=kb, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
