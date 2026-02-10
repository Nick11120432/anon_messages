from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import states as states
import keyboards as keyboards
import texts as t
from utils import safe_send_message

answer_message_router = Router()


@answer_message_router.message(states.Answer_message.receive_answer_message, F.text)
async def send_reply_text(message: Message, state: FSMContext, bot: Bot):
    """Отправление сообщения с текстом анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_message,
        chat_id=receiver_tg_id,
        text=t.reply_text(message.text),
        reply_to_message_id=reply_to_message_id,
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                bot.send_message,
                chat_id=receiver_tg_id,
                text=t.reply_text(message.text),
            )

        case _:
            pass

    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@answer_message_router.message(states.Answer_message.receive_answer_message, F.photo)
async def send_reply_photo(message: Message, state: FSMContext, bot: Bot):
    """Отправление фотографии анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_photo,
        chat_id=receiver_tg_id,
        photo=message.photo[-1].file_id,
        caption=t.reply_photo(message.caption or ""),
        reply_to_message_id=reply_to_message_id,
        reply_markup=answer_button,
        has_spoiler=True,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                bot.send_photo,
                chat_id=receiver_tg_id,
                photo=message.photo[-1].file_id,
                caption=t.reply_photo(message.caption or ""),
                has_spoiler=True,
            )

        case _:
            pass

    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@answer_message_router.message(states.Answer_message.receive_answer_message, F.video)
async def send_reply_video(message: Message, state: FSMContext, bot: Bot):
    """Отправление сообщения с видео анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_video,
        chat_id=receiver_tg_id,
        video=message.video.file_id,
        caption=t.reply_video(message.caption or ""),
        reply_to_message_id=reply_to_message_id,
        reply_markup=answer_button,
        has_spoiler=True,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                bot.send_video,
                chat_id=receiver_tg_id,
                video=message.video.file_id,
                caption=t.reply_video(message.caption or ""),
                has_spoiler=True,
            )

        case _:
            pass

    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@answer_message_router.message(
    states.Answer_message.receive_answer_message, F.animation
)
async def send_reply_animation(message: Message, state: FSMContext, bot: Bot):
    """Отправление сообщения с анимацией анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_animation,
        chat_id=receiver_tg_id,
        animation=message.animation.file_id,
        caption=t.reply_animation(message.caption or ""),
        reply_to_message_id=reply_to_message_id,
        reply_markup=answer_button,
        has_spoiler=True,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                bot.send_animation,
                chat_id=receiver_tg_id,
                animation=message.animation.file_id,
                caption=t.reply_animation(message.caption or ""),
                has_spoiler=True,
            )

        case _:
            pass

    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@answer_message_router.message(states.Answer_message.receive_answer_message, F.document)
async def send_reply_document(message: Message, state: FSMContext, bot: Bot):
    """Отправление сообщения с документом анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_document,
        chat_id=receiver_tg_id,
        document=message.document.file_id,
        caption=t.reply_document(message.caption or ""),
        reply_to_message_id=reply_to_message_id,
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                bot.send_document,
                chat_id=receiver_tg_id,
                document=message.document.file_id,
                caption=t.reply_document(message.caption or ""),
                has_spoiler=True,
            )

        case _:
            pass

    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@answer_message_router.message(states.Answer_message.receive_answer_message, F.voice)
async def send_reply_voice(message: Message, state: FSMContext, bot: Bot):
    """Отправление сообщения с голосовым анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_voice,
        chat_id=receiver_tg_id,
        voice=message.voice.file_id,
        caption=t.reply_voice(message.caption or ""),
        reply_to_message_id=reply_to_message_id,
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                bot.send_voice,
                chat_id=receiver_tg_id,
                voice=message.voice.file_id,
                caption=t.reply_voice(message.caption or ""),
                has_spoiler=True,
            )

        case _:
            pass

    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@answer_message_router.message(
    states.Answer_message.receive_answer_message, F.video_note
)
async def send_reply_video_note(message: Message, state: FSMContext, bot: Bot):
    """Отправление сообщения с видеозаписью анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_video_note,
        chat_id=receiver_tg_id,
        video_note=message.video_note.file_id,
        reply_to_message_id=reply_to_message_id,
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                bot.send_video_note,
                chat_id=receiver_tg_id,
                video_note=message.video_note.file_id,
                has_spoiler=True,
            )

        case _:
            pass

    await safe_send_message(
        bot.send_message,
        chat_id=receiver_tg_id,
        text=t.reply_video_note(),
    )
    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@answer_message_router.message(states.Answer_message.receive_answer_message, F.sticker)
async def send_reply_sticker(message: Message, state: FSMContext, bot: Bot):
    """Отправление сообщения со стикером анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_sticker,
        chat_id=receiver_tg_id,
        sticker=message.sticker.file_id,
        reply_to_message_id=reply_to_message_id,
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                bot.send_sticker,
                chat_id=receiver_tg_id,
                sticker=message.sticker.file_id,
                has_spoiler=True,
            )

        case _:
            pass

    await safe_send_message(
        bot.send_message,
        chat_id=receiver_tg_id,
        text=t.reply_sticker(),
    )
    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@answer_message_router.message(states.Answer_message.receive_answer_message)
async def send_reply_fallback(message: Message, state: FSMContext, bot: Bot):
    """Обработка других типов сообщений (audio, contact, location, etc.)."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        message.copy_to,
        chat_id=receiver_tg_id,
        reply_markup=answer_button,
        reply_to_message_id=reply_to_message_id,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return

        case "RespondMessageDeleted":
            await safe_send_message(
                message.copy_to,
                chat_id=receiver_tg_id,
                reply_markup=answer_button,
            )

        case _:
            pass

    await safe_send_message(
        bot.send_message,
        chat_id=receiver_tg_id,
        text=t.reply_text(message.text or ""),
    )

    await message.answer(t.REPLY_SENT_OK)
    await state.clear()
