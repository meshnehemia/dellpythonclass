class Shape:
    def draw(self):
        print("you are drawing a shape")


class Rectangle(Shape):
    def draw(self):
        print("drawing the rectangle")


class Square(Shape):
    def draw(self):
        print("drawing a square")


r = Rectangle()
s = Square()
r.draw()
s.draw()
