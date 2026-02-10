from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import states as states
import keyboards as keyboards
import texts as t
from utils import safe_send_message

send_message_router = Router()


@send_message_router.message(states.Send_message.receive_message, F.text)
async def send_anonymous_text(message: Message, state: FSMContext, bot: Bot):
    """Обработка отправки анонимного текстового сообщения."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_message,
        chat_id=receiver_tg_id,
        text=t.incoming_text(message.text),
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()


@send_message_router.message(states.Send_message.receive_message, F.photo)
async def send_anonymous_photo(message: Message, state: FSMContext, bot: Bot):
    """Отправка анонимного фото."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_photo,
        chat_id=receiver_tg_id,
        photo=message.photo[-1].file_id,
        caption=t.incoming_photo(message.caption or ""),
        reply_markup=answer_button,
        has_spoiler=True,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()


@send_message_router.message(states.Send_message.receive_message, F.video)
async def send_anonymous_video(message: Message, state: FSMContext, bot: Bot):
    """Отправка видео."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_video,
        chat_id=receiver_tg_id,
        video=message.video.file_id,
        caption=t.incoming_video(message.caption or ""),
        reply_markup=answer_button,
        has_spoiler=True,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()


@send_message_router.message(states.Send_message.receive_message, F.animation)
async def send_anonymous_animation(message: Message, state: FSMContext, bot: Bot):
    """Обработка анимации (GIF) и отправка её анонимно."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_animation,
        chat_id=receiver_tg_id,
        animation=message.animation.file_id,
        caption=t.incoming_animation(message.caption or ""),
        reply_markup=answer_button,
        has_spoiler=True,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()


@send_message_router.message(states.Send_message.receive_message, F.document)
async def send_anonymous_document(message: Message, state: FSMContext, bot: Bot):
    """Обработка отправки документов."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_document,
        chat_id=receiver_tg_id,
        document=message.document.file_id,
        caption=t.incoming_document(message.caption or ""),
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()


@send_message_router.message(states.Send_message.receive_message, F.voice)
async def send_anonymous_voice(message: Message, state: FSMContext, bot: Bot):
    """Отправка анонимного голосового сообщения."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_voice,
        chat_id=receiver_tg_id,
        voice=message.voice.file_id,
        caption=t.incoming_voice(message.caption or ""),
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()


@send_message_router.message(states.Send_message.receive_message, F.video_note)
async def send_anonymous_video_note(message: Message, state: FSMContext, bot: Bot):
    """Отправка видеозаметки (кружочка)."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_video_note,
        chat_id=receiver_tg_id,
        video_note=message.video_note.file_id,
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()


@send_message_router.message(states.Send_message.receive_message, F.sticker)
async def send_anonymous_sticker(message: Message, state: FSMContext, bot: Bot):
    """Отправка анонимного стикера."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        bot.send_sticker,
        chat_id=receiver_tg_id,
        sticker=message.sticker.file_id,
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()


@send_message_router.message(states.Send_message.receive_message)
async def send_anonymous_fallback(message: Message, state: FSMContext):
    """Обработка других типов сообщений (audio, contact, location, etc.)."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    result = await safe_send_message(
        message.copy_to,
        chat_id=receiver_tg_id,
        caption=t.incoming_text(message.caption or ""),
        reply_markup=answer_button,
    )

    match result:
        case "BotBlocked":
            await message.answer(t.USER_BLOCKED_BOT)
            await state.clear()
            return
        case _:
            pass

    await message.answer(t.SENT_OK)
    await state.clear()
