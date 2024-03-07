class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = tuple(dictionary.items())
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.dictionary):
            index = self.counter
            self.counter += 1
            return self.dictionary[index]
        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)