import numpy as np
import math

class invalidN(Exception):
    def __init__(self):
        super().__init__("N has to be a positive Integer")

class Number:
    def __init__(self, n):
        if not Number.validN(n):
            raise invalidN
        self.n = n

    @staticmethod
    def validN(n):
        if n > 0 and isinstance(n, int):
            return True
        return False

    def Nfactorial(self):
        N = self.n
        f = 1
        while N > 1:
            f *= N
            N -= 1
        return f


    def NFibonacci(self):

        result = np.array([0])
        if self.n == 1:
            return result
        result = np.append(result, [1])
        i = 2
        while i < self.n:
            result = np.append(result, [result[-1]+result[-2]])
            i+=1
        return result





def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1



