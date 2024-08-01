from src.io.config import Config
from src.io.git import Git

class DebugGitMessages():
    def __init__(self, config_filename, limit):
        cfg = Config(config_filename).get_config()
        self.__git = Git(cfg)
        self.__limit = limit

    def run(self):
        messages = self.__git.get_messages()
        return self.__print(messages)

    def __print(self, messages):
        result = []
        count = 0
        for item in messages:
            result.append(f'{item["hash"]} {item["value"]}')
            count += 1
            if self.__limit > 0 and count > self.__limit:
                break
        return result