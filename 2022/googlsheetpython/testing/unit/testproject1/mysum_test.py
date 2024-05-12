import unittest
from my_sum_testing import sum
# from fractions import Fraction
class TestSumFunctionallity(unittest.TestCase):
    def test_list_int(self):
        """
        Test : Can sum a list of int
         """
        data=[1,2,3]
        result = sum(data)
        self.assertEqual(result,6)
    # def test_list_fraction(self):
    #     """
    #     Test that it can sum a list of fractions
    #     """
    #     data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
    #     result = sum(data)
    #     self.assertEqual(result, 1)
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__=='__main__':
    unittest.main()