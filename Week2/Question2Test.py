import unittest

from Question2 import multAll2


class TestMultAll2(unittest.TestCase):
    def test_mutli_list(self):
        """
        Test that it multiply a list of integers
        """
        A=[5,12,31,7,25]
        k=10
        result = multAll2(A,k)
        self.assertEqual(result, [50,120,310,70,250])

if __name__ == '__main__':
    unittest.main()