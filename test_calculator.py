import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code
  def test_add(self):
    self.assertEqual(add(1, 2), 3)
    self.assertEqual(add(-2, 4), 2)
    self.assertEqual(add(0.1, 0.3), 0.4)
    
    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
  def test_subtraction(self):
    self.assertEqual(subtract(2, 1) 1)
    self.assertEqual(subtract(0, 7) -7)
    self.assertEqual(subtract(-3, -2) -1)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(4, 2), 8)
        self.assertEqual(multiply(2, 2), 4)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(4,2), 2)
        self.assertEqual(divide(8,4), 2)
        self.assertEqual(divide(9,3), 3)


    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError)
            square_root(-3)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(25), 5
  

# Do not touch this
if __name__ == "__main__":
    unittest.main()
