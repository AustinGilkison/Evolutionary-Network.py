import time, random, string

def map(value, start1, stop1, start2, stop2):
    numberRange = stop1-start1
    finalRange = stop2-stop1
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

def Accepted(length):
    accepted = string.ascii_letters + " "
    index = 0
    result = ""
    while index < length:
        result += random.choice(accepted)
        index += 1
    return result