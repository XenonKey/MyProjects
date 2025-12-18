import time
from functools import wraps


def timing(func):
    """Узнает время выполнения функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f'Function time: {end_time - start_time}')
        return result

    return wrapper


