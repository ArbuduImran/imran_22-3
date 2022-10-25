import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("ОК!")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Иди познавать python!")

async def wake_up():
    photo = open('media/mem3.jpg', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo,
                         caption="иди на урок!!!!!")



async def scheduler():
    aioschedule.every().saturday.at('16:00').do(go_to_sleep)
    aioschedule.every().saturday.at('16:00').do(wake_up)
    aioschedule.every().wednesday.at('16:00').do(go_to_sleep)
    aioschedule.every().wednesday.at('16:00').do(wake_up)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: "напомни" in word.text)
