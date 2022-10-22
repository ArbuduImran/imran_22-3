from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from database.bot_db import sql_command_random


async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Добро пожаловать в телеграмм бот {message.from_user.full_name}!\n"
                                                 f'"/quiz" - викторина из нескольких вопросов\n'
                                                 f'"/mem" - отправляет прикольные картирки\n'
                                                 f'"/mem2" - отпровляет еще одно фото\n'
                                                 f'"game - отправляет эмоджи"\n'
                                                 f'"/dice - игра против бота"\n'
                                                 f'"/reg - анкета"'
                           )


async def mems(message: types.Message):
    photo = open("media/mem.jpg", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


async def mems2(message: types.Message):
    photo = open("media/mem2.jpg", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


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


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('вы должны отвечать на сообщение')


async def get_random_mentor(message: types.Message):
    await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(get_random_mentor, commands=['get'])
    dp.register_message_handler(start_command, commands=['start', 'info'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mems, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
