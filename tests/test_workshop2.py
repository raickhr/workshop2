import sys
sys.path.append('../')

import pytest
import unittest

import numpy as np

from workshop2 import workshop2

class test_ckhr(unittest.TestCase):
    def test_calc_mean(self):
        assert workshop2.calc_mean(np.arange(1,20,2)) == 10
        assert workshop2.calc_mean(np.arange(-10,11,1)) == 0
        assert workshop2.calc_mean(np.ones(10)*10) == 10
        assert workshop2.answer == 5


if __name__ == '__main__':
    unittest.main()


