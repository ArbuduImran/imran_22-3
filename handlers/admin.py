import time
from aiogram import types, Dispatcher
from config import bot, dp, ADMIN


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


def register_handlers_ADMIN(dp: Dispatcher):
    dp.register_message_handler(dice, commands=['dice'])
