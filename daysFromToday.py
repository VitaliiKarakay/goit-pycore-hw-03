import datetime


def get_days_from_today(date):
    today = datetime.date.today()
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    return (today - date).days


print(get_days_from_today('2024-07-28'))