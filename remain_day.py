

def remain_date_input(nmonth ,nday):
    # print(dt.date.today())
    today = dt.date.today()
    print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
    # print(dt.datetime.now().replace(month=12 , day=25))
    return dt.datetime(2020,nmonth,nday)-dt.datetime.now()
nmonth = int(input('원하는 달을 입력하세요'))
nday = int(input('원하는 날을 입력하세요'))
print(remain_date_input(nmonth ,nday))