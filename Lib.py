import time
import random
import string


def map_v2(value, stop2):
    n = value*stop2
    x = n/stop2
    return x


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str(end - start))
        return result
    return wrapper


def accept(length):
    accepted = string.ascii_letters + " "
    index = 0
    result = ""
    while index < length:
        result += random.choice(accepted)
        index += 1
    return result
