""" In this module, there are Python subroutines to find the roots of a polynomial using
Newton Raphson method. """


def NewtonRaphson(fpoly, a, tolerance=1e-05, more_info=False):
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

     pseudocode:
     x = a
     while x > tol:
        x1 = x - f(x)/dfdx(x)
        x = x1
    """
    if check_poly_is_valid(fpoly):
        x = a
        df = derivative(fpoly)  # the derivative of the polynomial.
        ii = 0  # keep track of the number of iterations.
        while abs(polyval(fpoly, x)) > tolerance:
            if polyval(df, x) != 0:
                x = x - polyval(fpoly, x) / polyval(df, x)
            else:
                print("Newton method failed, dfdx=0")
            ii += 1

        if more_info:  # return more information about the iterative calculation.
            return x, polyval(fpoly, x), ii
        else:
            return x


def polyval(fpoly, x):
    """polyval(fpoly, x)
     Given a set of polynomial coefficients from highest order to x^0,
     compute the value of the polynomial at x. We assume zero
     coefficients are present in the coefficient list/tuple.
     Example: f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5
     polyval([4, 0, 9, 3], 5))
     returns 548
     """
    f_val = 0
    for ii in range(0, len(fpoly)):
        pwr = len(fpoly) - 1 - ii
        f_val = f_val + fpoly[ii] * (x ** pwr)
    return f_val


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
    dfdx = [None] * (len(fpoly) - 1)  # initialize list of coefficients for the derivative of fpoly.
    for ii in range(0, len(fpoly) - 1):
        dfdx[ii] = (len(fpoly) - 1 - ii) * fpoly[ii]
    return dfdx


def check_poly_is_valid(fpoly):
    """ check that the input for fpoly is valid. """
    if fpoly is []:
        print("fpoly is an empty list. ")
        return False
    elif fpoly is ():
        print("fpoly is an empty tuple. ")
        return False
    elif not any(isinstance(y, (int, float)) for y in fpoly):
        print("All elements in fpoly need to be type int or float.")
    else:
        return True


if __name__ == "__main__":
    fpoly = [2, 1, 2, 3]
    a = 1
    print("f(-1) = ", polyval(fpoly, -1))
    print("f(0) = ", polyval(fpoly, 0))
    print("f(1) = ", polyval(fpoly, 1))
    print("f(2) = ", polyval(fpoly, 2))
    print("df/dx = ", derivative(fpoly))
    print("local zero= ", NewtonRaphson(fpoly, a, tolerance=1e-05, more_info=True)[0])
    print("f(local zero)= ", NewtonRaphson(fpoly, a, tolerance=1e-05, more_info=True)[1])
    print("|f(local zero)|= ", abs(NewtonRaphson(fpoly, a, tolerance=1e-05, more_info=True)[1]))
    print("num of iterations= ", NewtonRaphson(fpoly, a, tolerance=1e-05, more_info=True)[2])

