import unittest
from src.core.config_default import config_default
from src.services.current_version_service import CurrentVersionService

class CurrentVersionServiceTests(unittest.TestCase):

    # run

    def __test__run(self, versions, exp):
        res = CurrentVersionService(config_default).run(versions)
        self.assertEqual(res, exp)

    def test__run__01(self):
        self.__test__run(
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
