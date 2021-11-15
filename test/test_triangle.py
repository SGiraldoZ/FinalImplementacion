import unittest
from figuras.modelo.triangle import Triangle, invalidSidesError


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_InvalidSides(self):
        with self.assertRaises(invalidSidesError):
            triangle = Triangle(8,1,1)
            triangle = Triangle(0,2,3)

    def test_triangle3_4_5(self):
        triangle = Triangle(3,4,5)
        self.assertEqual(triangle.area(), 6)
        self.assertEqual(triangle.perimeter(), 12)


if __name__ == '__main__':
    unittest.main()
