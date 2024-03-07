a = [1, 2, 3]
iter_a = iter(a)
print(iter_a)

print(next(iter_a))
print(next(iter_a))
print(next(iter_a))

# there is nothing left in iter_a, so it raise StopIteration Error
print(next(iter_a))
