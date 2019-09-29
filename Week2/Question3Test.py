import unittest

from Question3 import biggestIn


class TestBiggestIn(unittest.TestCase):
    def test_biggest_list(self):
        """
        Test that it can find the biggest integer in a list of integers
        """
        A=[5,12,31,7,25]
        result = biggestIn(A)
        self.assertEqual(result, 31)

if __name__ == '__main__':
    unittest.main()