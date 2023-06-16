class Fibonacci:
    def __init__(self):
        self.value0 = 0
        self.value1 = 1
        self.value2 = 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.value0 = self.value1 + self.value2
        self.value0, self.value1, self.value2 = self.value1, self.value2, self.value0
        self.index += 1
        return self.value0


fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
