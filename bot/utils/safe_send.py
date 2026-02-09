import asyncio
import logging

from aiogram.exceptions import (
    TelegramForbiddenError,
    TelegramBadRequest,
    TelegramRetryAfter,
)

logger = logging.getLogger(__name__)


async def safe_telegram_call(coroutine):
    """
    Выполняет Telegram API вызов и аккуратно обрабатывает типовые ошибки:
    - Forbidden: бот заблокирован / чат недоступен / пользователь удален
    - RetryAfter: лимиты Telegram (429)
    - BadRequest: некорректный запрос (reply_to не существует)
    """
    try:
        return await coroutine

    except TelegramRetryAfter as e:
        # Telegram просит подождать ровно retry_after секунд
        logger.warning("RetryAfter=%s", e.retry_after)
        await asyncio.sleep(e.retry_after)
        return await coroutine

    except TelegramForbiddenError:
        # Пользователь заблокировал бота или чат недоступен
        logger.warning("Forbidden: bot blocked or chat unavailable")
        return "BotBlocked"

    except TelegramBadRequest as e:
        logger.warning("BadRequest: %s", e)
        return "RespondMessageDeleted"
