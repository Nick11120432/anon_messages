# Общие
SELF_MESSAGE_FORBIDDEN = "Нельзя отправить сообщение самому себе xD"
INVALID_LINK_OR_USER = (
    "Данного пользователя не существует или ссылка недействительна :C"
)
USER_BLOCKED_YOU = "К сожалению пользователь вас заблокировал :C"
ADMIN_BLOCKED_YOU = "К сожалению администратор заблокировал вас :C"

PROMPT_ANON_MESSAGE = "Введи сообщение, которое хочешь отправить анонимно: "
PROMPT_REPLY_MESSAGE = "Введи сообщение которое хочешь отправить: "
FEEDBACK_MESSAGE = "Пожалуйста, введите ваш отзыв: "

SENT_OK = "Сообщение отправлено успешно!"
REPLY_SENT_OK = "Ответ отправлен успешно!"

BLACKLIST_CLEANED = "Черный список очищен!"
BLACKLIST_EMPTY = "Черный список пуст"

USER_BLOCKED_OK = "Пользователь заблокирован!\nРазблокировать: /clean_blacklist"

FEEDBACK_RECEIVED = "Спасибо за ваш отзыв! ❤️"
FEEDBACK_MESSAGE_INVALID = "Пожалуйста, введите отзыв текстом."


# Ссылки (HTML)
def my_link_full(link: str) -> str:
    return (
        "Твоя ссылка:\n\n"
        f"<code>{link}</code>\n\n"
        "Cкопируй её в профиль и жди сообщений ;)"
    )


def my_link_full_new(link: str) -> str:
    return (
        "Привет, рад видеть! Вот твоя новая ссылка:\n\n"
        f"<code>{link}</code>\n\n"
        "Cкопируй её в профиль и жди сообщений ;)"
    )


def my_link_short(link: str) -> str:
    return f"Твоя ссылка:\n<code>{link}</code>"


# Получатель: входящие сообщения
def incoming_text(text: str) -> str:
    return f"Кто-то отправил тебе сообщение!:\n\n{text}"


def incoming_photo(caption: str = "") -> str:
    return f"Кто-то отправил тебе изображение!\n\n{caption}".rstrip()


# Получатель: ответы
def reply_text(text: str) -> str:
    return f"Кто-то ответил тебе на сообщение!:\n\n{text}"


def reply_photo(caption: str = "") -> str:
    return f"Кто-то ответил тебе изображением!\n\n{caption}".rstrip()


# Обратная связь
def feedback_text(firstname: str, id: int, username: str, text: str) -> str:
    return (
        f'Пользователь <a href="tg://user?id={id}">{firstname}</a>\n'
        f"username: @{username}\n"
        f"id: {id}\n\n"
        f"Оставил текстовый отзыв:\n\n{text}"
    )


def feedback_text_select_action(firstname: str, id: int) -> str:
    return f"id пользователя: {id}\n\nВыберите действие с пользователем {firstname}:"


# Донат
DONATE_PROMPT_AMOUNT = "Введите сумму звезд, которую хотите отправить разработчику: 🥺"
DONATE_BAD_AMOUNT = "Пожалуйста, введите число не больше 100000"

INVOICE_TITLE = "Помощь разработчику"
INVOICE_DESCRIPTION = "Средства будут направлены на дальнейшую разработку! :3"
INVOICE_PAYLOAD = "Помощь разработчику"

PRECHECKOUT_ERROR = "Произошла ошибка, попробуйте ещё :C"
DONATE_THANKS = "Благодарим за пожертвование!❤️"

# Кнопки
BTN_BLOCK = "❌ Заблокировать"
BTN_RESPOND = "💬 Ответить"
