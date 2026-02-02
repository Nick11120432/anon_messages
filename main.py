import logging
import asyncio
import redis.asyncio as aioredis
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.types import BotCommand, BotCommandScopeDefault
from handlers.handlers import router
from handlers.callback_handlers import callback_router
from handlers.donate_handlers import donate_router
from database.models import async_main
from config_reader import config

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

redis_ip = config.redis_ip.get_secret_value()

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота 🚀"),
        BotCommand(command="profile", description="Моя ссылка 👤"),
        BotCommand(command="donate", description="Помочь разработчику ⭐")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())


async def main():
    redis = await aioredis.from_url(redis_ip)
    dp = Dispatcher(
        storage=RedisStorage(redis, key_builder=DefaultKeyBuilder(with_destiny=True))
    )
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_routers(router, callback_router, donate_router)
    await dp.start_polling(bot)

async def startup(bot: Bot):
    print("\033[32mstarting...\033[0m")
    await set_bot_commands(bot)
    await async_main()


async def shutdown():
    print("\033[33mshutting down...\033[0m")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\033[31mKeyboardInterrupt shutting down!\033[0m")
