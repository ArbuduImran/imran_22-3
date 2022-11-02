import asyncio

from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, admin, fsm_mentor, notifications, inline
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()

inline.inline_gogo_handler(dp)
client.register_handlers_client(dp)
admin.register_handlers_ADMIN(dp)
callback.callback_query_handler(dp)
fsm_mentor.register_handlers_fsm(dp)
notifications.register_handlers_notification(dp)



extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
