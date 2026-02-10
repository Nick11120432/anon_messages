import states as states
import keyboards as keyboards
import database.requests as requests
import texts as t
from config_reader import config

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram.filters import CommandStart, Command, CommandObject, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest


ADMIN_CHAT_ID = config.admin_chat_id


main_router = Router()


@main_router.message(CommandStart(deep_link=False), StateFilter("*"))
@main_router.message(Command("profile"))
async def start_handler(message: Message, bot: Bot, state: FSMContext):
    """Обработка обычного /start и /profile"""

    await state.clear()
    user_id = message.from_user.id

    link = await create_start_link(bot, f"{user_id}", encode=True)

    if await requests.check_user_exists(user_id):
        await message.answer(t.my_link_full(link))
    else:
        await requests.create_user_profile(user_id)
        await message.answer(t.my_link_full_new(link))

        
@main_router.message(CommandStart(deep_link=True), StateFilter("*"))
async def start_handler_with_link(
    message: Message, command: CommandObject, state: FSMContext
):
    """Обработка /start с параметром (глубокой ссылкой)."""
    await state.clear()

    try:
        payload = int(decode_payload(command.args))
    except (TypeError, ValueError):
        await message.answer(t.INVALID_LINK_OR_USER)
        return

    current_user_id = message.from_user.id

    if current_user_id == payload:
        await message.answer(t.SELF_MESSAGE_FORBIDDEN)
        return

    if not await requests.check_user_exists(payload):
        await message.answer(t.INVALID_LINK_OR_USER)
        return

    if await requests.check_if_user_blocked(
        owner_user_id=payload, blocked_user_id=current_user_id
    ):
        await message.answer(t.USER_BLOCKED_YOU)
        return

    await message.answer(t.PROMPT_ANON_MESSAGE)
    await state.set_state(states.Send_message.receive_message)
    await state.update_data(receive_message=payload)


@main_router.message(Command("clean_blacklist"), StateFilter("*"))
async def clean_blacklist(message: Message, state: FSMContext):
    """Очистка черного списка пользователя."""
    if await requests.clean_blacklist(message.from_user.id):
        await message.answer(t.BLACKLIST_CLEANED)
    else:
        await message.answer(t.BLACKLIST_EMPTY)


@main_router.message(Command("feedback"), StateFilter("*"))
async def feedback_handler(message: Message, state: FSMContext):
    """Начало процесса отправки отзыва."""
    if await requests.check_if_user_blocked(
        owner_user_id=ADMIN_CHAT_ID, blocked_user_id=message.from_user.id
    ):
        await message.answer(t.ADMIN_BLOCKED_YOU)
        return

    await state.set_state(states.Feedback_message.receive_feedback_message)
    await message.answer(t.FEEDBACK_MESSAGE)
    await state.update_data(receive_message=message.from_user.id)


@main_router.message(states.Feedback_message.receive_feedback_message)
async def receive_feedback(message: Message, state: FSMContext, bot: Bot):
    """Получение и отправка отзыва администратору."""
    if not message.text:
        await message.answer(t.FEEDBACK_MESSAGE_INVALID)
        return

    user = message.from_user

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    try:
        chat_info = await bot.get_chat(user.id)

        if not chat_info.has_private_forwards:
            await message.forward(chat_id=ADMIN_CHAT_ID)
            await bot.send_message(
                chat_id=ADMIN_CHAT_ID,
                text=t.feedback_text_select_action(
                    firstname=user.first_name, id=user.id
                ),
                reply_markup=answer_button,
            )
        else:
            await bot.send_message(
                chat_id=ADMIN_CHAT_ID,
                text=t.feedback_text(
                    firstname=user.first_name,
                    id=user.id,
                    username=user.username,
                    text=message.text,
                ),
                reply_markup=answer_button,
            )

    except TelegramBadRequest:
        await message.copy_to(chat_id=ADMIN_CHAT_ID)

    await message.answer(t.FEEDBACK_RECEIVED)
    await state.clear()
