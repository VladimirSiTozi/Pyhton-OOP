def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):
            result = func(num)
            wrapper.log[num] = result
        return wrapper.log[num]
    wrapper.log = {}
    return wrapper



@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(4)
print(fibonacci.log)