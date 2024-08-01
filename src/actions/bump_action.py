from providers.config import Config
from providers.bumper import Bumper

class BumpAction():
    def __init__(self, config_filename, version_str):
        self.__cfg = Config(config_filename).get_config()
        self.__bumper = Bumper()
        self.__version_str = version_str

    def run(self):
        result = ''
        for item in self.__cfg['bumps']:
            if result != '':
                result += '\n'
            filename = item['filename']
            self.__bumper.bump(filename, item['pattern'], self.__version_str)
            result += f'Bumped {filename} to {self.__version_str}'
        return result
