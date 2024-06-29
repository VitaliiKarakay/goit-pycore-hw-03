import re

country_code_w_plus = "+38"
country_code_wo_plus = "38"


def normalize_phone(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)
    if phone_number.startswith(country_code_wo_plus):
        phone_number = "+" + phone_number
    elif not phone_number.startswith(country_code_w_plus):
        phone_number = country_code_w_plus + phone_number

    return phone_number