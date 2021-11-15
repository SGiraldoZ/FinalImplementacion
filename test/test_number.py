import unittest

import numpy as np

from mathModule.modelo.Number import Number, invalidN
from numpy.testing import assert_array_equal

class MyTestCase(unittest.TestCase):
    def test_NotNaturalN(self):
       with self.assertRaises(invalidN):
           n = Number(0)
           n = Number(9.3)
           n = Number(-6)

    def test_normalN(self):
        n = Number(5)
        self.assertEqual(n.Nfactorial(), 120)
        assert_array_equal(n.NFibonacci(), np.array([0,1,1,2,3]))

    def test_bigN(self):
        n = Number(100)
        self.assertEqual(n.Nfactorial(), 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)






if __name__ == '__main__':
    unittest.main()
