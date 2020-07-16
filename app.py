import func_module as fm

#func_module.module_show()

nowdate = fm.date_now()
now_year = nowdate.year
now_month = nowdate.month
now_day = nowdate.day

now = '{}년 {}월 {}일'.format(now_year, now_month, now_day)

#print(nowdate)
#print(now)

x_mas = nowdate.replace(month = 12, day = 25)
x_mas_year = x_mas.year
x_mas_month = x_mas.month
x_mas_day = x_mas.day

x_mas_now = '{}년 {}월 {}일'.format(x_mas_year, x_mas_month, x_mas_day)
print(x_mas_now)