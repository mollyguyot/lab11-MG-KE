# https://github.com/keiraevnas/lab11-MG-KE
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def logarithm(base, value):
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and cannot equal 1")
    if value <= 0:
        raise ValueError("Value must be positive")
    return math.log(value, base)

def exp(a, b):
    return a ** b

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("Value must be positive")
    return math.sqrt(a)



