class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            current_i = self.i
            self.i -= 1
            return current_i
        raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print()
iterator1 = countdown_iterator(0)
for item in iterator1:
    print(item, end=" ")
