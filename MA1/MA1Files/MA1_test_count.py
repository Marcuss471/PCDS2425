# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        
        print('\nTests count')
        self.assertEqual(count(1, [1]), 1)
        
        #1. search empty lists
        self.assertEqual(count(1, []), 0)
        
        #2. count first, last and interior elements
        self.assertEqual(count(1, [1, 5, 2, 7, 333, 7, 3, 1]), 2)
        
        #3. search for a list
        self.assertEqual(count([1], [[], [2, [1], 1], 5]), 1)
        
        #4. check that sublists on several levels are searched
        self.assertEqual(count(1, [1, [2, 5, 1], 5, [1, [[4, 1], 3]],2]), 4)
        
        #5. search non existing elements
        self.assertEqual(count(1, [0, 6, 8, 3, 78]), 0)
        
        #6. check that the list searched is not destroyed
        self.assertEqual(count(1, [4, 1, 'a', 4, 1]) + count(1, [4, 1, 'a', 4, 1]), 4)


if __name__ == "__main__":
    unittest.main()
