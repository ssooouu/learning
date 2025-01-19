kb.add(bat_4)
kb_2 = ReplyKeyboardMarkup(resize_keyboard=True)
bat_1 = KeyboardButton(text='Мужчина')
bat_2 = KeyboardButton(text='Женщина')
kb_2.add(bat_1)
kb_2.add(bat_2)
kb_3 = InlineKeyboardMarkup(resize_keyboar=True)
bat_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
bat_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_3.add(bat_1)
kb_3.add(bat_2)
kb_4 = InlineKeyboardMarkup(resize_keyboar=True)
bat_1 = InlineKeyboardButton(text='Product1', callback_data="product_buying")
bat_2 = InlineKeyboardButton(text='Product2', callback_data="product_buying")
bat_3 = InlineKeyboardButton(text='Product3', callback_data="product_buying")
bat_4 = InlineKeyboardButton(text='Product4', callback_data="product_buying")
kb_4.add(bat_1)
kb_4.add(bat_2)
kb_4.add(bat_3)
kb_4.add(bat_4)


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    a = crud_functions.is_included(str(message.text))
    if a == False:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    if a == True:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_email(message, state):
    await state.update_data(age=message.text)
    await RegistrationState.age.set()
    data = await state.get_data()
    crud_functions.add_user(data['username'], data['email'], data['age'])
    await message.answer("Пользователь зарегистрирован!")
    await state.finish()



@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    prod = crud_functions.get_all_products()
    for g in prod:
        global c
        with open(f'{c}.jpg', 'rb') as img:
            c += 1
            await message.answer_photo(img, f'Название: {g[0]} | Описание: {g[1]} | Цена: {g[2]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_4)
    c = 1


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


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


@dp.message_handler(text='Информация')
async def set_male(message):
    await message.answer('Я бот помогающий тебе вычислить твою норму калорий!')
    await UserState.male.set()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
