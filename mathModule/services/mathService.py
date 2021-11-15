from ..modelo.Number import Number

def fibonacciService(n):
    num = Number(int(n))
    return num.NFibonacci()

def factorialService(n):
    num = Number(int(n))
    return num.Nfactorial()