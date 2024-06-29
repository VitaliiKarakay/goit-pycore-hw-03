import datetime

date_format = "%Y-%m-%d"
error_invalid_format = "Invalid date format. Please use YYYY-MM-DD."


def get_days_from_today(date):
    today = datetime.date.today()
    try:
        date = datetime.datetime.strptime(date, date_format).date()
        return (today - date).days
    except ValueError:
        return error_invalid_format
