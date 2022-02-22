class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

########################
    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            for height in range(self.height):
                picture += '*'.ljust(self.width, '*') + '\n'
        return picture
    def get_amount_inside(self, shape):
        fit = int(self.get_area() / shape.get_area())
        return fit
    def __str__(self):
        line = ''
        if self.width != self.height:
            line = 'Retangle' + '(width=' + str(self.width) + ', height=' + str(self.height) + ')'
        else:
            line = 'Square' + '(side=' + str(self.width) + ')'
        return line

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    def set_side(self, side):
        self.width = side
        self.height = side
######## debug for different input ########
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = width
        self.height = width

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())

sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

rect.set_width(7)
rect.set_height(8)
sq.set_side(2)
print(sq)


sq.set_width(4)
print(sq)
