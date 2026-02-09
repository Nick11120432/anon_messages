from .main_handlers import main_router
from .callback_handlers import callback_router
from .donate_handlers import donate_router
from .error_handlers import error_router

routers = [callback_router, donate_router, main_router, error_router]
