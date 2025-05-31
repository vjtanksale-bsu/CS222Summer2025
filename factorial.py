def Factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative values")
    if n == 0 or n == 1:
        return 1
    return n * Factorial(n - 1)
