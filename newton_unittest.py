"""" Unittest to validate the implementation of Newtons method in newtonraphson.py"""

import unittest
from newtonraphson import NewtonRaphson, derivative, polyval
from scipy import optimize


class TestNewton(unittest.TestCase):

    def test_ex1(self):
        """ compare the results of scipy vs my method. """
        f_possible = [[1, 2, 3, 4], [1, 1, 1, 1], [1, 20.2, 0], [1, 1, -1.01, 2]]
        for ii in range(0, len(f_possible)):
            function = f_possible[ii]
            x0 = 0
            f = lambda x: polyval(fpoly=function, x=x)
            root1 = optimize.newton(f, x0, tol=1e-05, disp=False)
            root2 = NewtonRaphson(fpoly=function, a=x0)
            print(abs(root1 - root2))
            self.assertTrue(abs(root1 - root2) < 1e-05)

    def test_ex2(self):
        """ compare the results of scipy vs my method. """
        f_possible = [[1, 2, 3, 4], [1, 1, 1, 1], [1, 20.2, 0], [1, 1, -1.01, 2]]
        for ii in range(0, len(f_possible)):
            function = f_possible[ii]
            x0 = complex(1, 1)
            root2 = NewtonRaphson(fpoly=function, a=x0)
            self.assertTrue(abs(polyval(function, root2)) < 1e-05)


if __name__ == '__main__':
    unittest.main()
