# https://github.com/keiraevans/lab-11-MG-KE
import math

def add(a, b):
    return a + b

def subtract(a, b):  # renamed
    return a - b

def mul(a, b):
    return a * b

def test_divide(self): 
    self.assertEqual(div(4, 2), 2) 
    self.assertEqual(div(8, 4), 2) 
    self.assertEqual(div(9, 3), 3) 

def test_divide_by_zero(self): 
with self.assertRaises(ValueError): 
    div(9, 0)

def logarithm(a, b):  # renamed
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


