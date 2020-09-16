""" In this module, there are Python subroutines to find the roots of a polynomial using
Newton Raphson method. """


def NewtonRaphson(fpoly, a, tolerance=.00001):
    """Given a set of polynomial coefficients fpoly
     for a univariate polynomial function,
     e.g. (3, 6, 0, -24) for 3x^3 + 6x^2 +0x^1 -24x^0,
     find the real roots of the polynomial (if any)
     using the Newton-Raphson method.
     a is the initial estimate of the root and
     starting state of the search
     This is an iterative method that stops when the
     change in estimators is less than tolerance.

     fpoly-list
     a-float
    """


def polyval(fpoly, x):
    """polyval(fpoly, x)
     Given a set of polynomial coefficients from highest order to x^0,
     compute the value of the polynomial at x. We assume zero
     coefficients are present in the coefficient list/tuple.
     Example: f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5
     polyval([4, 0, 9, 3], 5))
     returns 548
     """
    fval = 0
    for ii in range(0, len(fpoly)):
        pwr = len(fpoly) - 1 - ii
        fval = fval + fpoly[ii] * (x ** pwr)
    return fval


def derivative(fpoly):
    """derivative(fpoly)
     Given a set of polynomial coefficients from highest order to x^0,
     compute the derivative polynomial. We assume zero coefficients
     are present in the coefficient list/tuple.
     Returns polynomial coefficients for the derivative polynomial.
     Example:
     derivative((3,4,5)) # 3 * x**2 + 4 * x**1 + 5 * x**0
     returns: [6, 4] # 6 * x**1 + 4 * x**0
     """
    dfdx = [None] * (len(fpoly) - 1)
    for ii in range(0, len(fpoly) - 1):
        dfdx[ii] = (len(fpoly) - 1 - ii) * fpoly[ii]
    return dfdx
