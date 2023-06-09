class Shape:
    def __init__(self, Colour=str, Square=int):
        self.colour = Colour
        self.square = Square

    def set_colour(self, x):
        self.colour = x

    def request_colour(self):
        print(f"This shape is {self.colour}.")

    def set_square(self, x):
        self.square = x

    def request_square(self):
        print(f"This shape's area is {self.square}.")


a = Shape()

a.set_square(10)
a.set_colour('Red')

a.request_colour()
a.request_square()
