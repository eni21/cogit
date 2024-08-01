from src.io.config import Config

class ConfigAction():
    def __init__(self, config_filename):
        self.__config_filename = config_filename

    def run(self):
        return Config(self.__config_filename).get_config()
