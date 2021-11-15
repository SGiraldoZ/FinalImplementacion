import numpy as np
class sideSize0(Exception):
    def __init__(self):
        super().__init__("All the sides have to be longer than 0")

class Rectangle:
    def __init__(self, l1,l2):
        if not Rectangle.validRectangle(l1,l2):
            raise sideSize0
        self.l1 = l1
        self.l2 = l2

    @staticmethod
    def validRectangle(l1,l2):
        if l1 > 0 and l2 > 0:
            return True
        return False

    def area(self):
        return self.l1* self.l2


    def perimeter(self):
        if(self.l1 == 0 or self.l2 == 0):
            return 0
        return 2*(self.l1+self.l2)
