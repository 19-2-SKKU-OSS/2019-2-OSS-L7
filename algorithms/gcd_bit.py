from algorithms.bit import trailing_zero

"""
Given two positive integer a and b, computes the greatest common divisor of a and b
"""

def gcd_bit(a,b):
    tza=trailing_zero(a)
    tzb=trailing_zero(b)
    a>>=tza
    b>>=tzb
    while b:
        if a<b: a,b=b,a
        a-=b
        a>>=trailing_zero(a)
    return a<<min(tza,tzb)

