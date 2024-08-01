import os.path
import json
from src.core.merger import Merger
from src.core.config_default import config_default

class Config:
    def __init__(self, filename = None):
        self.__merger = Merger()
        self.__filename = filename if filename != None else 'cogit.json'
        self.__default = config_default

    def __read_json(self, filename):
        if os.path.isfile(filename):
            f = open(filename, 'r', encoding='utf-8')
            try:
                configJson = f.read()
                config = json.loads(configJson)
                return config
            finally:
                f.close()
        else:
            return {}

    def get_config(self):
        file = self.__read_json(self.__filename)
        result = self.__merger.merge_dicts(self.__default, file)
        return result
