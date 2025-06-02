import unittest
import tests.context
import os, shutil, glob
from src.providers.bumper import Bumper


class BumperTests(unittest.TestCase):
    def setUp(self):
        self.__bumper = Bumper()
        
        self.__file_dir = 'tests/files/test__bumper'
        self.__tmp_dir = 'tests/tmp/test_bumper' 
        if os.path.exists(self.__tmp_dir):
            shutil.rmtree(self.__tmp_dir)
        shutil.copytree(self.__file_dir, self.__tmp_dir)

        

    # bump

    def __test_bump(self, filename, pattern, version):
        self.__bumper.bump(filename, pattern, version)

    def test__is_bump__01(self):
        self.__test_bump(self.__tmp_dir + '/bump_01/*/*.csproj', '   <Version>{version}</Version>', '1.1.1')
