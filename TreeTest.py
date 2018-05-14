"""Unit tests for BinaryTree"""

import unittest
from BinaryTree import BinaryTree
from Bacteria import Bacteria

#Original values to pass in
_LENGTH = 1
_POS_X = 0
_POS_Y = 0
_AGE = 0


_TIM = Bacteria(_LENGTH, _POS_X, _POS_Y, _AGE, "timothy")
_TIM_TREE = BinaryTree(_TIM) #Tree with a lonely Timothy as root

class TreeTest(unittest.TestCase):

    def test_get_line_data(self):
        #Test for tree containing only Tim
        d = dict()
        _TIM_TREE._get_line_data(0, 1, d)
        answer_dict = {1:{0:_TIM}}
        self.assertDictEqual(d, answer_dict)

if __name__ == '__main__':
    unittest.main()
