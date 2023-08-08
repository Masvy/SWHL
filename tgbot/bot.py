import logging
import asyncio

from environs import Env
import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage


def setup_logging():
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s'
               ' [%(asctime)s] - %(name)s - %(message)s',
    )
    logger = logging.getLogger(__name__)
    logger.info('Starting bot')


async def main():
    setup_logging()

    storage: RedisStorage = RedisStorage.from_url('redis://localhost:6379/0',
                                                  key_builder=DefaultKeyBuilder(with_bot_id=True))

    env = Env()
    env.read_env()

    bot: Bot = Bot(token=env('BOT_TOKEN'),
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Stopping bot')