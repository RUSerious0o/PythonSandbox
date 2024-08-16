from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from bot_token import __token


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    data = {}


bot = Bot(token=__token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Calories', 'calories', 'c'])
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    UserState.data['age'] = message.text
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    UserState.data['growth'] = message.text
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    UserState.data['weight'] = message.text
    await state.finish()

    calories = (10 * float(UserState.data['weight']) +
                6.25 * float(UserState.data['growth']) -
                5 * float(UserState.data['age']) + 5)
    await message.answer(f'Ваша норма калорий: {round(calories, 1)}')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
