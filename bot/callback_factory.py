from aiogram.filters.callback_data import CallbackData


class RespondCallback(CallbackData, prefix="respond"):
    user_id: int
    message_id: int


class BlockCallback(CallbackData, prefix="block"):
    user_id: int
