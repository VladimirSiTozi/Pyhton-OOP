class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.small_circle = 0
        self.big_circle = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            if self.counter == len(self.sequence):
                current_index = 0
            else:
                current_index = self.counter - (len(self.sequence) * self.big_circle)
            self.counter += 1

            self.small_circle += 1
            if self.small_circle == 3:
                self.small_circle = 0
                self.big_circle += 1

            return self.sequence[current_index]
        raise StopIteration()


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

print()
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')