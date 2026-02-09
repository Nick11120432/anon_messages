import logging
import asyncio
import redis.asyncio as aioredis

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.types import BotCommand, BotCommandScopeDefault
from handlers import routers
from database import async_main
from config_reader import config
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger(__name__)

bot = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

redis_ip = config.redis_ip.get_secret_value()


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота 🚀"),
        BotCommand(command="profile", description="Моя ссылка 👤"),
        BotCommand(command="donate", description="Помочь разработчику ⭐"),
        BotCommand(command="clean_blacklist", description="Очистить черный список ❌"),
        BotCommand(command="feedback", description="Оставить отзыв 📝"),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())


async def main():
    redis = await aioredis.from_url(redis_ip)
    dp = Dispatcher(
        storage=RedisStorage(redis, key_builder=DefaultKeyBuilder(with_destiny=True))
    )
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_routers(*routers)
    await dp.start_polling(bot)


async def startup(bot: Bot):
    logger.info("Starting up...")
    await set_bot_commands(bot)
    await async_main()


async def shutdown():
    logger.warning("Shutting down...")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.error("KeyboardInterrupt shutting down!")
