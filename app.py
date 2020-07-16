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


def remain_date_input(nmonth ,nday):
    # print(dt.date.today())
    today = dt.date.today()
    print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
    # print(dt.datetime.now().replace(month=12 , day=25))
    return dt.datetime(2020,nmonth,nday)-dt.datetime.now()
nmonth = int(input('원하는 달을 입력하세요'))
nday = int(input('원하는 날을 입력하세요'))
print(remain_date_input(nmonth ,nday))



