from callback_factory import AnswerCallbackFactory
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    InlineKeyboardButton
)


async def create_answer_button(user_id, message_id):
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text="❌ Заблокировать",
            callback_data=AnswerCallbackFactory(action="block", user_id=str(user_id), message_id="").pack()
        ),
        InlineKeyboardButton(
            text="💬 Ответить",
            callback_data=AnswerCallbackFactory(action="respond", user_id=str(user_id), message_id=str(message_id)).pack()
        )
    )
    return builder.as_markup()