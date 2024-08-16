from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from bot_token import __token


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    data = {}


bot = Bot(token=__token)
dp = Dispatcher(bot, storage=MemoryStorage())
reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Рассчитать'),
        KeyboardButton('Информация')
    ]
], resize_keyboard=True)
inline_keyboard = InlineKeyboardMarkup()
inline_keyboard.add(InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'))
inline_keyboard.add(InlineKeyboardButton(text='Формулы расчета', callback_data='formulas'))


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer(text='Выберите опцию', reply_markup=inline_keyboard)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    text = ('1. Упрощенный вариант формулы Миффлина-Сан Жеора:\n'
            'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n'
            'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.message.answer(text=text)
    await call.answer()


@dp.message_handler(commands=['start'])
async def start_bot(message):
    await message.answer(text='Привет! Я бот, помогающий твоему здоровью.', reply_markup=reply_keyboard)


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст')
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
