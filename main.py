import asyncio
from aiogram import types

import logging
from bot import bot, dp, scheduler
from handlers import (
    start_router,
    myinfo_router,
    picture_router,
    shop_router,
    free_lesson_form_router,
    questions_router,
    delayed_answer_router,
    echo_router
)
from db.queries import init_db, create_tables, populate_tables


async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="начало"),
        types.BotCommand(command="myinfo", description="информация обо мне"),
        types.BotCommand(command="pic", description="показать картинку"),
        types.BotCommand(command="shop", description="магазин"),
        types.BotCommand(command="free_lesson", description="Записаться на открытый урок"),
        types.BotCommand(command="quest", description="опросник"),
        types.BotCommand(command="remind", description="напоминалка"),
        types.BotCommand(command="echo", description="эхо")
    ])

    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)
    dp.include_router(free_lesson_form_router)
    dp.include_router(questions_router)
    dp.include_router(delayed_answer_router)

    dp.startup.register(on_startup)
    dp.include_router(echo_router)
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())