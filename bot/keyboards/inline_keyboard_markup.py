from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

import datetime
import calendar


calendar_cb = CallbackData('calendar', 'action', 'date')


def create_calendar(year=None, month=None):
    months = {
        'January': 'Январь', 'February': 'Февраль', 'March': 'Март', 'April': 'Апрель',
        'May': 'Май', 'June': 'Июнь', 'July': 'Июль', 'August': 'Август',
        'September': 'Сентябрь', 'October': 'Октябрь', 'November': 'Ноябрь', 'December': 'Декабрь'
    }
    markup = InlineKeyboardMarkup(row_width=7)
    now = datetime.datetime.now()
    year = now.year if not year else year
    month = now.month if not month else month

    markup.row(
        InlineKeyboardButton(months.get(calendar.month_name[month])+" "+str(year), callback_data="ignore")
    )

    days_of_week = []
    for day in ["ПОН", "ВТ", "СР", "ЧЕТ", "ПЯТ", "СУБ", "ВС"]:
        days_of_week.append(InlineKeyboardButton(day, callback_data="ignore"))
    markup.row(*days_of_week)

    my_calendar = calendar.monthcalendar(year, month)
    for week in my_calendar:
        for day in week:
            if day == 0:
                markup.insert(InlineKeyboardButton(" ", callback_data="ignore"))
            else:
                callback_data = calendar_cb.new(action='day', date=".".join([str(day), str(month), str(year)]))
                markup.insert(InlineKeyboardButton(str(day), callback_data=callback_data))

    markup.row(
        InlineKeyboardButton("<", callback_data=calendar_cb.new(action="prev", date=".".join([str(month), str(year)]))),
        InlineKeyboardButton(" ", callback_data="ignore"),
        InlineKeyboardButton(">", callback_data=calendar_cb.new(action="next", date=".".join([str(month), str(year)])))
        )
    return markup
