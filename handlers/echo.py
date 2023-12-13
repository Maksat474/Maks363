from aiogram import Router, F, types


echo_router = Router()


@echo_router.message(F.text)
async def echo(message: types.Message):
    await message.answer(message.text)