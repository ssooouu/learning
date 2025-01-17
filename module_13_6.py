from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    male = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
bat_1 = KeyboardButton(text='Рассчитать')
bat_2 = KeyboardButton(text='Информация')
kb.add(bat_1)
kb.add(bat_2)
kb_2 = ReplyKeyboardMarkup(resize_keyboard=True)
bat_1 = KeyboardButton(text='Мужчина')
bat_2 = KeyboardButton(text='Женщина')
kb_2.add(bat_1)
kb_2.add(bat_2)
kb_3 = InlineKeyboardMarkup(resize_keyboar=True)
bat_1 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
bat_2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
kb_3.add(bat_1)
kb_3.add(bat_2)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=kb_3)


@dp.message_handler(text='Информация')
async def set_male(message):
    await message.answer('Я бот помогающий тебе вычислить твою норму калорий!')


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула расчета для мужчин:\n'
                              '10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161. \n'
                              'Формула расчета для женщин:\n '
                              '10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_male(call):
    await call.message.answer('Выберите свой пол: ', reply_markup=kb_2)
    await call.answer()
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
        await message.answer(
            f"Ваша норма калорий: {10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161}")
        await state.finish()


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Информация')
async def set_male(message):
    await message.answer('Я бот помогающий тебе вычислить твою норму калорий!')
    await UserState.male.set()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)