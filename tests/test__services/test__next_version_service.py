import unittest
import tests.context
from core.config_default import config_default
from services.next_version_service import NextVersionService

class NextVersionServiceTests(unittest.TestCase):

    # run

    def __test__run(self, messages, versions, exp):
        res = NextVersionService(config_default).run(messages, versions)
        self.assertEqual(res, exp)

    def test__run__01(self):
        self.__test__run(messages=[
            {
                'hash': '05',
                'value': 'message5',
            },
            {
                'hash': '04',
                'value': 'message4',
            },
            {
                'hash': '03',
                'value': 'message3',
            },
            {
                'hash': '02',
                'value': 'message2',
            },
            {
                'hash': '01',
                'value': 'message1',
            },
        ],
        versions=[
            {
                'hash': '04',
                'value': '0.0.2',
            },
            {
                'hash': '02',
                'value': '0.0.1',
            }
        ],
        exp='0.0.2')

    def test__run__02(self):
        self.__test__run(messages=[
            {
                'hash': '05',
                'value': 'fix: message5',
            },
            {
                'hash': '04',
                'value': 'message4',
            },
            {
                'hash': '03',
                'value': 'message3',
            },
            {
                'hash': '02',
                'value': 'message2',
            },
            {
                'hash': '01',
                'value': 'message1',
            },
        ],
        versions=[
            {
                'hash': '04',
                'value': '0.0.2',
            },
            {
                'hash': '02',
                'value': '0.0.1',
            }
        ],
        exp='0.0.3')


    def test__run__03(self):
        self.__test__run(messages=[
            {
                'hash': '05',
                'value': 'feat: message5',
            },
            {
                'hash': '04',
                'value': 'message4',
            },
            {
                'hash': '03',
                'value': 'message3',
            },
            {
                'hash': '02',
                'value': 'message2',
            },
            {
                'hash': '01',
                'value': 'message1',
            },
        ],
        versions=[
            {
                'hash': '04',
                'value': '0.0.2',
            },
            {
                'hash': '02',
                'value': '0.0.1',
            }
        ],
        exp='0.1.0')

    def test__run__04(self):
        self.__test__run(messages=[
            {
                'hash': '05',
                'value': 'feat!: message5',
            },
            {
                'hash': '04',
                'value': 'message4',
            },
            {
                'hash': '03',
                'value': 'message3',
            },
            {
                'hash': '02',
                'value': 'message2',
            },
            {
                'hash': '01',
                'value': 'message1',
            },
        ],
        versions=[
            {
                'hash': '04',
                'value': '0.0.2',
            },
            {
                'hash': '02',
                'value': '0.0.1',
            }
        ],
        exp='1.0.0')