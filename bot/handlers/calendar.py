from datetime import datetime, timedelta
from typing import Dict, Any

from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from keyboards.inline_keyboard_markup import create_calendar, calendar_cb


async def calendar_handler(query: CallbackQuery,  callback_data: Dict[str, Any]):
    action = callback_data['action']
    month, year = callback_data['date'].split('.')
    current = datetime(int(year), int(month), 1)
    new_period = current - timedelta(days=1) if action == 'prev' else current + timedelta(days=31)
    await query.message.edit_text(
        'Выберите день:',
        reply_markup=create_calendar(int(new_period.year), int(new_period.month))
    )


async def chosen_day(query: CallbackQuery,  callback_data: Dict[str, Any]):
    day, month, year = callback_data['date'].split('.')
    await query.answer('Выбрана дата: {}'.format(datetime(int(year), int(month), int(day)).strftime('%d.%m.%Y')))


def register_switch_period(dp: Dispatcher):
    dp.register_callback_query_handler(
        calendar_handler,
        calendar_cb.filter(action=['prev', 'next']),
    )
    dp.register_callback_query_handler(
        chosen_day,
        calendar_cb.filter(action=['day'])
    )


