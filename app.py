import func_module as fm

#func_module.module_show()

nowdate = fm.date_now()

#print(nowdate)

now_year = nowdate.year
now_month = nowdate.month
now_day = nowdate.day

now = '{}년 {}월 {}일'.format(now_year, now_month, now_day)
#print(now)

x_mas = nowdate.replace(month = 12, day = 25)
x_mas_year = x_mas.year
x_mas_month = x_mas.month
x_mas_day = x_mas.day

x_mas_now = '{}년 {}월 {}일'.format(x_mas_year, x_mas_month, x_mas_day)
#print(x_mas_now)

import datetime as dt

today = dt.date.today()
#print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))

time_gap = x_mas - dt.datetime.now()
#print("남은날 = {}월 {}일".format(time_gap.days, time_gap.seconds))






