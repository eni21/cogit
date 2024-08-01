import unittest
import tests.context
from src.core.config_default import config_default
from src.core.git_parser import GitParser
from src.core.semver import Semver

class GetParserTests(unittest.TestCase):
    def setUp(self):
        self.git_parser = GitParser(config_default)
        self.semver = Semver(config_default)

    # parse_messages

    def __test__parse_messages(self, input, exp):
        res = self.git_parser.parse_messages(input)
        self.assertListEqual(res, exp)

    def test__parse_messages__01(self):
        self.__test__parse_messages(
            input='''
"0005 message5"
"0004 message4"
"0003 message3"
"0002 message2"
"0001 message1"
''',
            exp=[
                {
                'hash':'0005',
                'value':'message5',
                },
                {
                'hash':'0004',
                'value':'message4',
                },
                {
                'hash':'0003',
                'value':'message3',
                },
                {
                'hash':'0002',
                'value':'message2',
                },
                {
                'hash':'0001',
                'value':'message1',
                },
            ])

    # parse_versions

    def __test__parse_versions(self, input, exp):
        res = self.git_parser.parse_versions(input)
        self.assertListEqual(res, exp)

    def test__parse_versions__01(self):
        self.__test__parse_versions(
            input='''
"0005 (HEAD -> dev, origin/dev)"
"0004 (tag: 0.0.2)"
"0003 "
"0002 (tag: 0.0.1, origin/master, origin/HEAD, master)"
"0001 "
''',
            exp=[
                {
                    'hash':'0004',
                    'value': '0.0.2',
                },
                {
                    'hash':'0002',
                    'value': '0.0.1',
                }
            ])
