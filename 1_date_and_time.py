"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))


from datetime import datetime
from datetime import time, timedelta 


dt_now = datetime.now()
delta1 = timedelta(days=1)
yesterday = dt_now - delta1

delta2 = timedelta(days=30)
month_ago = dt_now - delta2
print(f'сегодня {dt_now}')
print(f'вчера {yesterday}')
print(f'месяц назад {month_ago}')

import locale
ru_dt = locale.setlocale(locale.LC_TIME, "ru_Ru")
date_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(f'datetime {date_dt}')
