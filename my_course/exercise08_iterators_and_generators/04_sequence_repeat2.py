class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            idx = self.counter % len(self.sequence)
            self.counter += 1
            return self.sequence[idx]
        raise StopIteration()


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')

print()
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
