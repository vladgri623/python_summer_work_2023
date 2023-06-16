class Person(object):
    def __init__(self, full_name):
        self.lname = full_name.split()[0]
        self.name = full_name.split()[1]
        self.fname = full_name.split()[2]

    def __repr__(self):
        return f"Person: {self.lname} {self.name} {self.fname}"

    def __str__(self):
        return f"{self.lname}{self.name}{self.fname}"[::-1]


p = Person(input('Введите ФИО: '))
print(p)
