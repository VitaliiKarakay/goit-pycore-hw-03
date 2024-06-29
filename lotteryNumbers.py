import random


def get_number_tickets(min_number, max_number, quantity):
    if not params_validate(max_number, min_number, quantity):
        return []
    numbers = random.sample(range(min_number, max_number + 1), quantity)

    return sorted(numbers)


def params_validate(max_number, min_number, quantity):
    return min_number < max_number or min_number > 1 or max_number < 1000 or quantity > 1

