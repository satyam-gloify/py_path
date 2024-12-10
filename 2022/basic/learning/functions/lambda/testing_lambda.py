import unittest
#################UNIT TEST
addtwo = lambda a:a+2

class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2),4)
    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2),4.2)
    def test_add_three(self):
        # Should fail
        self.assertEqual(addtwo(3),6)

if __name__=='__main__':
    unittest.main(verbosity=2)


####################DOCTEST

doctest

# The doctest module extracts interactive Python code from docstring to execute tests. Although the syntax of Python lambda functions does not support a typical docstring, it is possible to assign a string to the __doc__ element of a named lambda:

addtwo = lambda x: x + 2
addtwo.__doc__ = """Add 2 to a number.
    >>> addtwo(2)
    4
    >>> addtwo(2.2)
    4.2
    >>> addtwo(3) # Should fail
    6
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
# The doctest in the doc comment of lambda addtwo() describes the same test cases as in the previous section.

# When you execute the tests via doctest.testmod(), you get the following:
# The failed test results from the same failure explained in the execution of the unit tests in the previous section.

# You can add a docstring to a Python lambda via an assignment to __doc__ to document a lambda function. Although possible, the Python syntax better accommodates docstring for normal functions than lambda functions.

# For a comprehensive overview of unit testing in Python, you may want to refer to Getting