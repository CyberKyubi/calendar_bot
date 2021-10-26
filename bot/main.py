import logging
import asyncio
from logging.config import dictConfig

from aiogram import Bot, Dispatcher

from handlers import register_handlers
from utils.logging_config import config
from config import load_config


async def main():
    logging.getLogger(__name__)
    dictConfig(config)

    bot_config = load_config()

    bot = Bot(bot_config.token)
    dp = Dispatcher(bot)

    register_handlers(dp)

    try:
        logging.warning("Bot started!")
        await dp.start_polling(allowed_updates=["message", "callback_query"])
    except Exception as error:
        logging.error(error)
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()

        await bot.session.close()
        logging.warning("All session was closed!")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.error('Bot is stopped!')
