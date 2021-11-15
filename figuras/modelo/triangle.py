import numpy as np
class invalidSidesError(Exception):
    def __init__(self):
        self.message = "A triangle cannot exist with 3 sides of those sizes. For any 2 sides, the sum of their sizes have to be bigger than the third"
        super().__init__(self.message)

class Triangle:
    def __init__(self, l1,l2,l3):
        if (not Triangle.validTriangle(l1,l2,l3)):
            raise invalidSidesError

        self.l1 = l1
        self.l2 = l2
        self.l3 = l3


    @staticmethod
    def validTriangle(l1, l2, l3):
        if (l1+l2<= l3 or l1+l3<= l2 or l3+l2<= l1):
            return False
        return True


    def area(self):
        s = (self.l1+self.l2+self.l3)/2
        area = np.sqrt((s*(s -self.l1)*(s-self.l2)*(s-self.l3)))

        return area

    def perimeter(self):
        return self.l1+self.l2+self.l3

