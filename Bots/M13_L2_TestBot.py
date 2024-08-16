from pprint import pprint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from bot_token import __token


bot = Bot(token=__token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print(f'Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    print(f'Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
