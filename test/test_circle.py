import unittest
from figuras.modelo.circle import Circle, invalidRadiusError
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_Circle2(self):
        circle = Circle(2)
        self.assertEqual(circle.area(), np.pi*4)  # add assertion here
        self.assertEqual(circle.perimeter(), np.pi*4)

    def test_CircleInvalid(self):
        with self.assertRaises(invalidRadiusError):
            circle = Circle(0)
            circle = Circle(-2)


    def test_Circle33(self):
        circle = Circle(33)
        self.assertEqual(circle.area(), np.pi*(33**2))



if __name__ == '__main__':
    unittest.main()
