# Общие
SELF_MESSAGE_FORBIDDEN = "Ой 😅 Самому себе отправить нельзя."
INVALID_LINK_OR_USER = "Упс 😔 Пользователь не найден или ссылка недействительна."
USER_BLOCKED_YOU = "Не получится 😕 Пользователь добавил вас в чёрный список."
ADMIN_BLOCKED_YOU = "К сожалению 😔 Администратор ограничил вам доступ."

PROMPT_ANON_MESSAGE = "✉️ Напиши сообщение, которое хочешь отправить анонимно:"
PROMPT_REPLY_MESSAGE = "💬 Напиши ответ, который хочешь отправить:"
FEEDBACK_MESSAGE = "📝 Пожалуйста, напиши свой отзыв:"

SENT_OK = "✅ Сообщение отправлено!"
REPLY_SENT_OK = "✅ Ответ отправлен!"

BLACKLIST_CLEANED = "🧹 Чёрный список очищен!"
BLACKLIST_EMPTY = "📭 Чёрный список пуст."

USER_BLOCKED_OK = "🚫 Пользователь заблокирован.\n🔓 Разблокировать: /clean_blacklist"

FEEDBACK_RECEIVED = "Спасибо за отзыв! ❤️"
FEEDBACK_MESSAGE_INVALID = "Пожалуйста, отправь отзыв текстом 📝"


# Ссылки (HTML)
def my_link_full(link: str) -> str:
    return (
        "🔗 Твоя личная ссылка:\n\n"
        f"<code>{link}</code>\n\n"
        "Скопируй её в профиль/сторис и получай анонимные сообщения 😉"
    )


def my_link_full_new(link: str) -> str:
    return (
        "Привет! 👋 Рад видеть тебя здесь 😊\n"
        "Вот твоя личная ссылка:\n\n"
        f"<code>{link}</code>\n\n"
        "Скопируй её в профиль/сторис и получай анонимные сообщения 😉"
    )


def my_link_short(link: str) -> str:
    return f"🔗 Твоя ссылка:\n<code>{link}</code>"


# Получатель: входящие сообщения
def incoming_text(text: str) -> str:
    return f"📩 Тебе пришло анонимное сообщение:\n\n{text}"


def incoming_photo(caption: str = "") -> str:
    caption = caption.strip()
    if caption:
        return f"🖼️ Тебе прислали изображение:\n\n{caption}"
    return "🖼️ Тебе прислали изображение!"


# Получатель: ответы
def reply_text(text: str) -> str:
    return f"↩️ Тебе ответили на сообщение:\n\n{text}"


def reply_photo(caption: str = "") -> str:
    caption = caption.strip()
    if caption:
        return f"↩️ Тебе ответили изображением:\n\n{caption}"
    return "↩️ Тебе ответили изображением!"


# Обратная связь (HTML)
def feedback_text(firstname: str, id: int, username: str, text: str) -> str:
    username_line = f"@{username}" if username and username != "(no username)" else "—"
    return (
        f'📝 <b>Новый отзыв</b>\n'
        f'👤 Пользователь: <a href="tg://user?id={id}">{firstname}</a>\n'
        f"🔗 Username: {username_line}\n"
        f"🆔 ID: <code>{id}</code>\n\n"
        f"💬 Текст:\n\n{text}"
    )


def feedback_text_select_action(firstname: str, id: int) -> str:
    return (
        f"🛠️ Управление пользователем\n"
        f"🆔 ID: <code>{id}</code>\n"
        f"👤 Пользователь: {firstname}\n\n"
        f"Выберите действие 👇"
    )


# Донат
DONATE_PROMPT_AMOUNT = "⭐️ Сколько звёзд хочешь отправить разработчику? (введи число) 🥺"
DONATE_BAD_AMOUNT = "⚠️ Введи, пожалуйста, число до 100000."

INVOICE_TITLE = "Поддержать разработчика 💛"
INVOICE_DESCRIPTION = "Спасибо! Это помогает развивать проект 🚀"
INVOICE_PAYLOAD = "donate_support"

PRECHECKOUT_ERROR = "Упс 😔 Что-то пошло не так. Попробуй ещё раз."
DONATE_THANKS = "Спасибо за поддержку! ❤️⭐️"


# Кнопки
BTN_BLOCK = "🚫 Заблокировать"
BTN_RESPOND = "💬 Ответить"
