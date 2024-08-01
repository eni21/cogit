import unittest
import tests.context
from core.merger import Merger

class MergerTests(unittest.TestCase):
    # merge_dicts

    def __test__merge_dicts(self, a, b, exp):
        res = Merger().merge_dicts(a, b)
        self.assertDictEqual(res, exp)

    def test__merge_dicts__01(self):
        a = {'aaa': {'1': 1,'2': 2}}
        b = {'aaa': {'1':123}}
        exp = {'aaa': {'1': 123,'2': 2}}
        self.__test__merge_dicts(a, b, exp)
