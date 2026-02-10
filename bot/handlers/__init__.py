from .main_handlers import main_router
from .callback_handlers import callback_router
from .donate_handlers import donate_router
from .error_handlers import error_router
from .send_message_handlers import send_message_router
from .answer_message_handlers import answer_message_router

routers = [
    main_router,
    callback_router,
    donate_router,
    send_message_router,
    answer_message_router,
    error_router,
]
