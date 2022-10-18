import random

from aiogram import types, Dispatcher
from config import bot, dp


async def echo(message: types.Message):
    if message.text.startswith('game'):
        list_game = ['⚽', '️🏀', '🎲', '🎰', '🎳', '🎯']
        await bot.send_dice(message.chat.id, emoji=random.choice(list_game))
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
