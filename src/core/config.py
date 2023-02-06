import os.path
import json

class Config:
    def __init__(self, filename = None):
        self.__filename = filename if filename != None else 'cogit.json'
        self.__default = {
            'cwd': '.',
            'branch': 'master',
            'pattern': '{major}.{minor}.{patch}',
            'bumps': [],
            'types': [
                'build',
                'chore',
                'ci',
                'docs',
                'feat',
                'fix',
                'perf',
                'refactor',
                'revert',
                'style',
                'test'
            ],
        }

    def __read_json(self, filename):
        if os.path.isfile(filename):
            f = open(filename, 'r', encoding="utf-8")
            configJson = f.read()
            config = json.loads(configJson)
            return config
        else:
            return {}

    def __merge_dicts(self, a, b):
        result = a.copy()
        result.update(b)
        return result

    def get_config(self):
        file = self.__read_json(self.__filename)
        result = self.__merge_dicts(self.__default, file)
        return result
