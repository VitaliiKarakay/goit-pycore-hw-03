import datetime

import constants


def adjust_for_weekend(date):
    if date.weekday() == 5:
        return date + datetime.timedelta(days=2)
    elif date.weekday() == 6:  # If Sunday
        return date + datetime.timedelta(days=1)
    else:
        return date


def get_upcoming_birthdays(users):
    today = datetime.datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], constants.date_format_dot).date()
        birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)
        days_to_birthday = (birthday_this_year - today).days
        if 0 <= days_to_birthday <= 7:
            birthday_this_year = adjust_for_weekend(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"],
                                       "congratulation_date": birthday_this_year.strftime(constants.date_format_dot)})
    return upcoming_birthdays
