# https://github.com/keiraevans/lab-11-MG-KE
import math

def add(a, b):
    return a + b

def sub(a, b):  # renamed
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):  # renamed
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and cannot equal 1")
    if b <= 0:
        raise ValueError("Value must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("Value must be positive")
    return math.sqrt(a)


