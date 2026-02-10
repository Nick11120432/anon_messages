import asyncio
import logging
from typing import Any, Awaitable, Callable

from aiogram.exceptions import (
    TelegramForbiddenError,
    TelegramBadRequest,
    TelegramRetryAfter,
)

logger = logging.getLogger(__name__)

TelegramCallable = Callable[..., Awaitable[Any]]


async def safe_send_message(fn: TelegramCallable, /, **kwargs) -> str | None:
    """
    Безопасно выполняет Telegram API вызов (fn(**kwargs)) и обрабатывает типовые ошибки.

    Возвращает:
      - "BotBlocked"            -> Forbidden (бот заблокирован / чат недоступен / пользователь удалён)
      - "RespondMessageDeleted" -> BadRequest (обычно reply_to_message_id не существует)
      - None                    -> успех
    """
    try:
        await fn(**kwargs)
        return None

    except TelegramRetryAfter as e:
        logger.warning("RetryAfter=%s", e.retry_after)
        await asyncio.sleep(e.retry_after)

        try:
            await fn(**kwargs)
            return None
        except TelegramForbiddenError:
            logger.warning("Forbidden after retry: bot blocked or chat unavailable")
            return "BotBlocked"
        except TelegramBadRequest as e2:
            logger.warning("BadRequest after retry: %s", e2)
            return "RespondMessageDeleted"

    except TelegramForbiddenError:
        # Пользователь заблокировал бота или чат недоступен
        logger.warning("Forbidden: bot blocked or chat unavailable")
        return "BotBlocked"

    except TelegramBadRequest as e:
        # Пользователь удалил сообщение оригинальное сообщение
        logger.warning("BadRequest: %s", e)
        return "RespondMessageDeleted"
