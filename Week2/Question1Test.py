import unittest

from Question1 import multAll


class TestMultAll(unittest.TestCase):
    def test_mutli_list(self):
        """
        Test that it multiply a list of integers
        """
        A=[5,12,31,7,25]
        k=10
        result = multAll(A,k)
        self.assertEqual(result, [50,120,310,70,250])

if __name__ == '__main__':
    unittest.main()