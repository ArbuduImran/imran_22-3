import time
from aiogram import types, Dispatcher
from config import bot, dp, ADMIN
from database.bot_db import sql_command_all
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def dice(message: types.Message):
    if message.from_user.id in ADMIN:
        await bot.send_message(message.from_user.id, 'DICE PLAYER')
        a = await bot.send_dice(message.from_user.id, emoji='🎲')
        await message.answer('-' * 25)
        await bot.send_message(message.from_user.id, 'DICE BOT')
        b = await bot.send_dice(message.from_user.id, emoji='🎲')
        time.sleep(4)
        if a.dice.value > b.dice.value:
            await message.answer('playr win')
        elif b.dice.value > a.dice.value:
            await message.answer('bot win')
        else:
            await message.answer('draw')
    else:
        pass


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer('Ты не АДМИН!')
    else:
        mentors = await sql_command_all()
        for mentor in mentors:
            await bot.send_message(message.chat.id, f'ID: {mentor[0]}\n'
                                                    f'Name: {mentor[1]}\n'
                                                    f'Direction: {mentor[2]}\n'
                                                    f'Age: {mentor[3]}\n'
                                                    f'Group: {mentor[4]}',
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f'Delete {mentor[1]}', callback_data=f'delete {mentor[0]}')
                                   ))


def register_handlers_ADMIN(dp: Dispatcher):
    dp.register_message_handler(dice, commands=['dice'])
    dp.register_message_handler(delete_data, commands=['del'])