import datetime

import constants


def get_days_from_today(date):
    today = datetime.date.today()
    try:
        date = datetime.datetime.strptime(date, constants.date_format).date()
        return (today - date).days
    except ValueError:
        return constants.error_invalid_format
