"""This is a test to check the Validity of the funtion in sudoku.py"""

import unittest

from sudoku import check_sum
class TestSudoku(unittest):
    def test_sudoku(self):
        self.assertTrue(check_sum() == 45) # Checks that the function returns 45
        self.assertGreater(check_sum(),0) # Checks that the function should return a positive number

if __name__ == '__main__':
    unittest.main()
    
