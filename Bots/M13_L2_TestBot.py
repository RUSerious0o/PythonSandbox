from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from bot_token import __token
from aiogram.dispatcher import FSMContext
from aiogram.types.message import Message


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


bot = Bot(token=__token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Calories', 'calories', 'c'])
async def set_age(message, state):
    await message.answer('Введите свой возраст')
    await state.set_state(UserState.age)


@dp.message_handler(state=UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await state.set_state(UserState.growth)


@dp.message_handler(state=UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await state.set_state(UserState.weight)


@dp.message_handler(state=UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.finish()

    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(message.text)
    calories = 10 * weight + 6.25 * growth - 5 * age

    await message.answer(f'Ваша норма калорий: {round(calories, 1)}')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
