import numpy as np

class invalidRadiusError(Exception):
    def __init__(self):
        super().__init__("Radius has to be greater than 0")


class Circle:
    def __init__(self, r):
        if not Circle.validCircle(r):
            raise invalidRadiusError
        self.r = r

    @staticmethod
    def validCircle(r):
        if r <= 0:
            return False
        return True

    def area(self):
        area = np.pi*self.r**2
        return area

    def perimeter(self):
        perimeter = 2*np.pi*self.r
        return perimeter

