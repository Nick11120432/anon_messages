import asyncio
import logging

from rich.logging import RichHandler
from aiogram import Router
from aiogram.types import ErrorEvent
from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramForbiddenError,
    TelegramNetworkError,
    TelegramRetryAfter,
    TelegramAPIError,
)

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

error_router = Router()


@error_router.error()
async def global_error_handler(event: ErrorEvent) -> bool:
    """
    Глобальный обработчик ошибок.
    Возвращаем True -> ошибка считается обработанной.
    """
    exc = event.exception

    # 429 Too Many Requests
    if isinstance(exc, TelegramRetryAfter):
        logger.warning("TelegramRetryAfter: %s sec ", exc.retry_after)
        # В error handler повторять запрос нельзя (мы не знаем какой запрос), но можно чуть подождать
        await asyncio.sleep(min(exc.retry_after, 5))
        return True

    # 403 Forbidden: bot blocked / chat not found / user deactivated etc.
    if isinstance(exc, TelegramForbiddenError):
        logger.info("TelegramForbiddenError: %s", exc)
        return True

    # 400 Bad Request: некорректный параметр (reply_to не существует, message not modified, etc.)
    if isinstance(exc, TelegramBadRequest):
        logger.warning("TelegramBadRequest: %s", exc)
        return True

    # сетевые проблемы
    if isinstance(exc, TelegramNetworkError):
        logger.warning("TelegramNetworkError: %s", exc)
        return True

    # любые другие Telegram API ошибки
    if isinstance(exc, TelegramAPIError):
        logger.exception("TelegramAPIError: %s", exc)
        return True

    # вообще любые другие исключения
    logger.exception("Unhandled exception: %s", exc)
    return True
