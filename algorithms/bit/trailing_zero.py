"""
Given a positive integer x, computes the number of trailing zero of x.
Example)
Input : 34(100010)
           ~~~~~^
Output : 1

Input : 40(101000)
           ~~~^^^
Output : 3
"""

def trailing_zero(x):
    cnt=0
    while x and not x&1:
        cnt+=1
        x>>=1
    return cnt


