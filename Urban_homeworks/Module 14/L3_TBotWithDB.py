import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from bot_token import __token
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import L4_ProductsDB_ORM


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


dp = Dispatcher(storage=MemoryStorage())

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='Информация')
    ],
    [
        KeyboardButton(text='Купить')
    ]
], resize_keyboard=True)

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
    ]
])

inline_buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 4', callback_data='product_buying'),
        ]
    ]
)


@dp.message(CommandStart())
async def start_bot(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text='Привет! Я бот, помогающий твоему здоровью.', reply_markup=reply_keyboard)


@dp.message(F.text == 'Рассчитать')
async def show_main_menu(message: Message):
    await message.answer(text='Выберите опцию', reply_markup=inline_keyboard)


@dp.message(F.text == 'Купить')
async def get_buying_list(message: Message):
    products = L4_ProductsDB_ORM.get_all_products()
    for product in products:
        caption_ = f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}'
        await message.answer_photo(photo=FSInputFile(product[4]), caption=caption_)
    await message.answer(text='Выберите продукт для покупки:', reply_markup=inline_buy_menu)


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer(text='Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    text = ('1. Упрощенный вариант формулы Миффлина-Сан Жеора:\n'
            'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n'
            'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.message.answer(text=text)
    await call.answer()


@dp.callback_query(F.data == 'calories')
async def set_age(call: CallbackQuery, state: FSMContext):
    print(call.__class__)
    await call.message.answer('Введите свой возраст')
    await call.answer()
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()

    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(message.text)
    calories = 10 * weight + 6.25 * growth - 5 * age

    await message.answer(f'Ваша норма калорий: {round(calories, 1)}')


async def main():
    bot = Bot(token=__token)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    L4_ProductsDB_ORM.initiate_db()
    asyncio.run(main())
