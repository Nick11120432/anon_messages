from aiogram.fsm.state import State, StatesGroup


class Send_message(StatesGroup):
    receive_message = State()


class Answer_message(StatesGroup):
    receive_answer_message = State()


class Feedback_message(StatesGroup):
    receive_feedback_message = State()


class Donate(StatesGroup):
    amount = State()
