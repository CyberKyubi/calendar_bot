from aiogram import Dispatcher

from .cmd_start import register_cmd_start
from .calendar import register_switch_period


def register_handlers(dp: Dispatcher):
    register_cmd_start(dp)
    register_switch_period(dp)