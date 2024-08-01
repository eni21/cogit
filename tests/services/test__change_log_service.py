import unittest
from src.services.change_log_service import ChangeLogService

class ChangeLogServiceTests(unittest.TestCase):
    # run

    def __test__run(self, messages, versions, limit, exp):
        res = ChangeLogService().run(messages, versions, limit)
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
        limit=0,
        exp='''*new*

\tmessage5

0.0.2

\tmessage4
\tmessage3

0.0.1

\tmessage2
\tmessage1
''')
        
    def test__run__02(self):
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
        limit=2,
        exp='''*new*

\tmessage5

0.0.2

\tmessage4
\tmessage3
''')
