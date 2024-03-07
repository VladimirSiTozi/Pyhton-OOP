def genrange(start: int, end: int):
    for i in range(start, end + 1):
        yield i

    # current = start
    # while current <= end:
    #         yield current
    #         current += 1

x = list(genrange(1, 10))
print(x)

print(list(genrange(1, 10)))

