import datetime


def get_days_from_today(date):
    today = datetime.date.today()
    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return (today - date).days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
