from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import logging



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Добро пожаловать в телеграмм бот {message.from_user.full_name}!\n"
                                                 f'"/quiz" - викторина из нескольких вопросов\n'
                                                 f'"/mem" - отправляет прикольные картирки\n'
                                                 f'"/mem2" - отпровляет еще одно фото'
                           )


@dp.message_handler(commands=['mem'])
async def mems(call: types.CallbackQuery):
    photo = open("media/Prishel-s-raboty.jpg", 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)


@dp.message_handler(commands=['mem2'])
async def mems(message: types.Message):
    photo = open("media/прикольная-картинка-2.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'В каком году был осонован Geektech?'
    answers = [
        '2016',
        "1989",
        "2019",
        "2001",
        "2018",
        "Еще до нашей эры"
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="не шаришь!",
        open_period=25,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'самая длинная река К-Р?'
    answers = [
        "нил",
        "Нарын",
        "Чу",
        "Чаткал?",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Учи географию",
        open_period=15,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_3')
async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("NEXT", callback_data='button_call_4')
    markup.add(button_call_4)
    question = 'АТВЕЧААААЙ!'
    answers = [
        'незнаю',
        '5, 8',
        '11, 8',
        '12, 9',
        '0',
    ]
    photo = open('media/задачка.jpeg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="2-й класс...",
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
