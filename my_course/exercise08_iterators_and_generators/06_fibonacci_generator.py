def fibonacci():
    num_a, num_b = 0, 1
    while True:
        yield num_a
        num_a, num_b = num_b, num_a + num_b


generator = fibonacci()
for i in range(5):
    print(next(generator))
