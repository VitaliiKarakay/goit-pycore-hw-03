import random


def get_number_tickets(min_number, max_number, quantity):
    return random.sample(range(min_number, max_number), quantity)
