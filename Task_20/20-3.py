class NumUpper:
    def __init__(self):
        self.letter = 64
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.letter += 1
        self.number += 1
        if self.number == 27:
            self.letter = 65
            self.number = 1
        return str(self.number) + ', ' + str(chr(self.letter))


inst = NumUpper()
for i in inst:
    print(i, end=', ')
