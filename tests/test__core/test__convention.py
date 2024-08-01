import unittest
import tests.context
from src.core.config_default import config_default
from src.core.convention import Convention

class ConventionTests(unittest.TestCase):
    def setUp(self):
        self.__convention = Convention(config_default)

    # is_major

    def __test__is_major(self, msg, exp):
        res = self.__convention.is_major(msg)
        self.assertEqual(res, exp)

    def test__is_major__01(self):
        self.__test__is_major('some message', False)

    def test__is_major__02(self):
        self.__test__is_major('chore: some message', False)

    def test__is_major__03(self):
        self.__test__is_major('chore(api): some message', False)

    def test__is_major__04(self):
        self.__test__is_major('chore!: some message', True)

    def test__is_major__05(self):
        self.__test__is_major('chore fix!: some message', True)

    def test__is_major__06(self):
        self.__test__is_major('chore fix!: some message', True)

    def test__is_major__07(self):
        self.__test__is_major('chore_fix!: some message', True)

    def test__is_major__08(self):
        self.__test__is_major('chore-fix!: some message', True)

    def test__is_major__09(self):
        self.__test__is_major('chore (api)!: some message', True)

    def test__is_major__10(self):
        self.__test__is_major('chore(api web)!: some message', True)

    def test__is_major__11(self):
        self.__test__is_major('chore(api_web)!: some message', True)

    def test__is_major__12(self):
        self.__test__is_major('chore(api-web)!: some message', True)

    # is_minor

    def __test__is_minor(self, msg, exp):
        res = self.__convention.is_minor(msg)
        self.assertEqual(res, exp)

    def test__is_minor__01(self):
        self.__test__is_minor('some message', False)

    def test__is_minor__02(self):
        self.__test__is_minor('fix: some message', False)

    def test__is_minor__03(self):
        self.__test__is_minor('fix(api): some message', False)

    def test__is_minor__04(self):
        self.__test__is_minor('fix (api): some message', False)

    def test__is_minor__05(self):
        self.__test__is_minor('feat: some message', True)

    def test__is_minor__06(self):
        self.__test__is_minor('feat(api): some message', True)

    def test__is_minor__07(self):
        self.__test__is_minor('feat (api): some message', True)

    # is_patch

    def __test__is_patch(self, msg, exp):
        res = self.__convention.is_patch(msg)
        self.assertEqual(res, exp)

    def test__is_patch__01(self):
        self.__test__is_patch('some message', False)

    def test__is_patch__02(self):
        self.__test__is_patch('chore: some message', False)

    def test__is_patch__03(self):
        self.__test__is_patch('chore!: some message', False)

    def test__is_patch__04(self):
        self.__test__is_patch('chore(api): some message', False)

    def test__is_patch__05(self):
        self.__test__is_patch('chore(api)!: some message', False)

    def test__is_patch__06(self):
        self.__test__is_patch('fix: some message', True)

    def test__is_patch__07(self):
        self.__test__is_patch('fix(api): some message', True)

    def test__is_patch__08(self):
        self.__test__is_patch('fix (api): some message', True)

    def test__is_patch__09(self):
        self.__test__is_patch('fix(api web): some message', True)
    
    def test__is_patch__10(self):
        self.__test__is_patch('fix (api)!: some message', False)
