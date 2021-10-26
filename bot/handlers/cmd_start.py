from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline_keyboard_markup import create_calendar


async def cmd_start(message: Message):
    await message.answer('Выберите день:', reply_markup=create_calendar())


def register_cmd_start(dp: Dispatcher):
    dp.register_message_handler(
        cmd_start,
        CommandStart(),
    )


