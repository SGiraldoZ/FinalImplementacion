import unittest
from figuras.modelo.rectangle import Rectangle, sideSize0


class MyTestCase(unittest.TestCase):

    def test_invalidRectangle(self):
        with self.assertRaises(sideSize0):
            rectangle = Rectangle(3,0)
            rectangle = Rectangle(-2, 5)

    def test_rectangle4_5(self):
        rectangle = Rectangle(5,4)
        self.assertEqual(rectangle.area(), 20)
        self.assertEqual(rectangle.perimeter(), 18)


if __name__ == '__main__':
    unittest.main()
