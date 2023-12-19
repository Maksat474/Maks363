from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


free_lesson_form_router = Router()


class Form(StatesGroup):
    name = State()
    age = State()
    age = State()
    direction = State()
    phone = State()


@free_lesson_form_router.message(Command("free_lesson"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Как Вас зовут?")


@free_lesson_form_router.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    if len(message.text) < 3:
        await message.answer("Слишком короткое имя")
    else:
        await state.update_data(name=message.text)
        await message.answer(f"Спасибо, {message.text}")

        await state.set_state(Form.age)
        await message.answer("Сколько вам лет?")


@free_lesson_form_router.message(Form.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть числом!")
    elif int(age) < 13 or int(age) > 80:
        await message.answer("Возраст должен быть от 12 до 100")
    else:
        await state.update_data(age=int(age))
        await state.set_state(Form.direction)
        await message.answer("По какому направлению вы хотите учиться?")