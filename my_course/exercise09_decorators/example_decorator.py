import logging

def log(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args} and kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def my_function(x, y):
    return x + y

print(my_function(10, 2))