from src.io.config import Config
from src.io.bumper import Bumper

class BumpAction():
    def __init__(self, config_filename, version_str):
        self.__cfg = Config(config_filename).get_config()
        self.__bumper = Bumper()
        self.__version_str = version_str

    def run(self):
        for item in self.__cfg['bumps']:
            self.__bumper.bump(item['filename'], item['pattern'], self.__version_str)
