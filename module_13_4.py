from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    male = State()


@dp.message_handler(text='Calories')
async def set_male(message):
    await message.answer('Введите свой пол (Мужчина или Женщина): ')
    await UserState.male.set()

@dp.message_handler(state=UserState.male)
async def set_age(message, state):
    await state.update_data(male=message.text)
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    if data['male'] == 'Мужчина':
        await message.answer(f"Ваша норма калорий: {10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5}")
        await state.finish()
    else:
        await message.answer(f"Ваша норма калорий: {10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161}")
        await state.finish()

@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
