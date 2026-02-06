# Общие
SELF_MESSAGE_FORBIDDEN = "Ой 😅 <b>Самому себе</b> отправить нельзя."
INVALID_LINK_OR_USER = "Упс 😔 <b>Пользователь не найден</b> или ссылка <i>недействительна</i>."
USER_BLOCKED_YOU = "Не получится 😕 <b>Пользователь</b> добавил вас в <i>чёрный список</i>."
ADMIN_BLOCKED_YOU = "К сожалению 😔 <b>Администратор</b> ограничил вам доступ."

PROMPT_ANON_MESSAGE = "✉️ <b>Напиши сообщение</b>, которое хочешь отправить <i>анонимно</i>:"
PROMPT_REPLY_MESSAGE = "💬 <b>Напиши ответ</b>, который хочешь отправить:"
FEEDBACK_MESSAGE = "📝 <b>Оставь отзыв</b> (только текстом):"

SENT_OK = "✅ <b>Готово!</b> Сообщение отправлено."
REPLY_SENT_OK = "✅ <b>Готово!</b> Ответ отправлен."

BLACKLIST_CLEANED = "🧹 <b>Чёрный список очищен!</b>"
BLACKLIST_EMPTY = "📭 <i>Чёрный список пуст.</i>"

USER_BLOCKED_OK = (
    "🚫 <b>Пользователь заблокирован.</b>\n"
    "🔓 Разблокировать: /clean_blacklist"
)

FEEDBACK_RECEIVED = "Спасибо за отзыв! ❤️ <i>Мы обязательно посмотрим.</i>"
FEEDBACK_MESSAGE_INVALID = "Пожалуйста, отправь отзыв <b>текстом</b> 📝"


# Ссылки (HTML)
def my_link_full(link: str) -> str:
    return (
        "🔗 <b>Твоя личная ссылка</b>\n"
        "━━━━━━━━━━━━━━\n\n"
        f"<code>{link}</code>\n\n"
        "📌 Скопируй её в профиль/сторис и получай <i>анонимные</i> сообщения 😉"
    )


def my_link_full_new(link: str) -> str:
    return (
        "Привет! 👋 <b>Рад видеть тебя здесь</b> 😊\n\n"
        "🔗 <b>Твоя личная ссылка</b>\n"
        "━━━━━━━━━━━━━━\n\n"
        f"<code>{link}</code>\n\n"
        "📌 Скопируй её в профиль/сторис и получай <i>анонимные</i> сообщения 😉"
    )


def my_link_short(link: str) -> str:
    return f"🔗 <b>Твоя ссылка:</b>\n<code>{link}</code>"


# Получатель: входящие сообщения
def incoming_text(text: str) -> str:
    return (
        "📩 <b>Тебе пришло анонимное сообщение</b>\n"
        "━━━━━━━━━━━━━━\n\n"
        f"{text}"
    )


def incoming_photo(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "🖼️ <b>Тебе прислали изображение</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "🖼️ <b>Тебе прислали изображение</b>."


# Получатель: ответы
def reply_text(text: str) -> str:
    return (
        "↩️ <b>Тебе ответили</b> на сообщение\n"
        "━━━━━━━━━━━━━━\n\n"
        f"{text}"
    )


def reply_photo(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "↩️ <b>Тебе ответили изображением</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "↩️ <b>Тебе ответили изображением</b>."


# Обратная связь (HTML)
def feedback_text(firstname: str, id: int, username: str, text: str) -> str:
    username_line = f"@{username}" if username and username != "(no username)" else "<i>не указан</i>"
    return (
        "📝 <b>Новый отзыв</b>\n"
        "━━━━━━━━━━━━━━\n"
        f'👤 Пользователь: <a href="tg://user?id={id}"><b>{firstname}</b></a>\n'
        f"🔗 Username: {username_line}\n"
        f"🆔 ID: <code>{id}</code>\n\n"
        "💬 <b>Текст:</b>\n"
        f"{text}"
    )


def feedback_text_select_action(firstname: str, id: int) -> str:
    return (
        "🛠️ <b>Управление пользователем</b>\n"
        "━━━━━━━━━━━━━━\n"
        f"🆔 ID: <code>{id}</code>\n"
        f"👤 Пользователь: <b>{firstname}</b>\n\n"
        "<i>Выберите действие 👇</i>"
    )


# Донат (HTML)
DONATE_PROMPT_AMOUNT = "⭐️ <b>Сколько звёзд</b> хочешь отправить разработчику? <i>(введи число)</i> 🥺"
DONATE_BAD_AMOUNT = "⚠️ Введи, пожалуйста, <b>число</b> от 1 до <code>100000</code>."

INVOICE_TITLE = "Поддержать разработчика 💛"
INVOICE_DESCRIPTION = "Спасибо! Это помогает развивать проект 🚀"
INVOICE_PAYLOAD = "donate_support"

PRECHECKOUT_ERROR = "Упс 😔 <b>Ошибка оплаты</b>. Попробуй ещё раз."
DONATE_THANKS = "Спасибо за поддержку! ❤️⭐️ <i>Это очень помогает.</i>"


# Кнопки (обычный текст, HTML не нужен)
BTN_BLOCK = "🚫 Заблокировать"
BTN_RESPOND = "💬 Ответить"
