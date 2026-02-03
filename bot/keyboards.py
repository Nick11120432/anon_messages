from callback_factory import RespondCallback, BlockCallback
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

import texts as t


async def create_answer_button(user_id, message_id):
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text=t.BTN_BLOCK,
            callback_data=BlockCallback(
                action="block", user_id=user_id, message_id=0
            ).pack(),
        ),
        InlineKeyboardButton(
            text=t.BTN_RESPOND,
            callback_data=RespondCallback(
                action="respond", user_id=user_id, message_id=message_id
            ).pack(),
        ),
    )
    return builder.as_markup()
