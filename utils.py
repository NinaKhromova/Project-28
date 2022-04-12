import string
import random


def get_random_string(string_length):
    return ''.join(random.choices(string.ascii_uppercase, k=string_length))


def get_random_number(a, b):
    return random.randint(a, b)
