a = [1, 2, 3]
iter_a = iter(a)
print(iter_a)

while True:
    try:
        print(next(iter_a))
    except StopIteration:
        break
