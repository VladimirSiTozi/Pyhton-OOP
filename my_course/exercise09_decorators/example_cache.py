import functools

def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'cache'):
            wrapper.cache = {}
        key = tuple(args) + tuple(kwargs.items())
        if key in wrapper.cache:
            result = wrapper.cache[key]
        else:
            result = func(*args, **kwargs)
            wrapper.cache[key] = result
        return result
    return wrapper

@cache
def my_function(x, y):
    return x + y

my_function(1, 2)
print(my_function(1, 2))