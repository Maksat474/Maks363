from aiogram import Router, F, types
from aiogram.filters import Command
from bot import bot, scheduler


delayed_answer_router = Router()


@delayed_answer_router.message(Command("remind"))
async def reminder(message: types.Message):
     await message.answer("I will remind you every day")
     scheduler.add_job(
        send_reminder,
         trigger="interval",
         day=1,
         kwargs={"chat_id": message.from_user.id}
    )


async def send_reminder(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text="Сделать домашнее задание!!!"
    )