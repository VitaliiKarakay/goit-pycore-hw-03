import random

import constants


def get_number_tickets(min_number, max_number, quantity):
    if not params_validate(max_number, min_number, quantity):
        return []
    numbers = random.sample(range(min_number, max_number + 1), quantity)

    return sorted(numbers)


def params_validate(max_number, min_number, quantity):
    return (min_number < max_number or min_number > constants.const_min_number or
            max_number < constants.const_max_number or quantity > constants.const_min_quantity)
