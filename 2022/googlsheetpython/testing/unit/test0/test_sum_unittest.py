import unittest

class TestSum(unittest.TestCase):

    def test_Sum(self):
        self.assertEqual(sum([1,2,3]),6,'Should be 6')
    
    def test_Sum_Tuple(self):
        self.assertEqual(sum((1,2,1)),4,'Should be 4')

if __name__== '__main__':
    unittest.main()