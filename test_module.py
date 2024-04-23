import unittest

from module import square, double


class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2), 4) # test when 2 is given as input, the output is 4
        self.assertEqual(square(3.0), 9.0) # test when 3.0 is given with an output of 9.0
        self.assertNotEqual(square(-3), -9) 

class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
unittest.main()