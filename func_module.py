import datetime as dt


def module_show():
    module_type = dir(datetime)
    print(module_type)

def date_now():
    return dt.datetime.now()