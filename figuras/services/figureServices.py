
from ..modelo.circle import Circle, invalidRadiusError
from ..modelo.triangle import Triangle
from ..modelo.rectangle import Rectangle

def circleService(r):
    circle = Circle(int(r))
    return {"radius": r, "area": circle.area(), "perimeter": circle.perimeter()}

def triangleService(l1, l2, l3):
    triangle = Triangle(int(l1), int(l2), int(l3))
    return {"l1": triangle.l1, "l3": triangle.l3, "l2": triangle.l2, "area": triangle.area(), "perimeter": triangle.perimeter()}

def rectangleService(l1, l2):
    rectangle = Rectangle(int(l1), int(l2))
    return {"l1": rectangle.l1, "l2": rectangle.l2, "area": rectangle.area(), "perimeter": rectangle.perimeter()}