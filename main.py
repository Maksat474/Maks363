import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from aiogram.filters import Command
import random
from pathlib import Path
import logging

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}")


@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    user_info = (
        f"Ваш id: {message.from_user.id}\n"
        f"Имя: {message.from_user.first_name}\n"
        f"Username: @{message.from_user.username}"
    )
    await message.answer(user_info)


@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    image_directory = Path("images")
    image_files = list(image_directory.iterdir())
    random_image = random.choice(image_files)
    file = types.FSInputFile(random_image)

    await message.answer_photo(
        photo=file
    )


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="начало"),
        types.BotCommand(command="myinfo", description="информация обо мне"),
        types.BotCommand(command="pic", description="показать картинку")
    ])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())