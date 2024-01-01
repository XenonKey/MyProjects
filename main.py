from libs import *
from libs2 import *
import sys
import time

def my_decorator(func):
    def wrapper(x):
        start_time = time.time()
        func(x)
        end_time = time.time()
        return f'Время перебора типа {type(x)}: {end_time - start_time}'
    return wrapper



lst = [x for x in range(100000000)]
gen = (x for x in range(100000000))


def count_range(iter):
    loc_count = 0
    for i in iter:
        loc_count += 1
    return loc_count

count_range = my_decorator(count_range)

print(count_range(lst))
print(count_range(gen))
