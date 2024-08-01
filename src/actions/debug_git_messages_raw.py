from src.io.config import Config
from src.io.git import Git

class DebugGitMessagesRaw():
    def __init__(self, config_filename, limit):
        cfg = Config(config_filename).get_config()
        self.__git = Git(cfg)
        self.__limit = limit

    def run(self):
        string = self.__git.get_messages_raw()
        return self.__print(string)
    
    def __print(self, string):
        lines = string.split('\n')
        result = ''
        count = 0
        for line in lines:
            result += line + '\n'
            count += 1
            if self.__limit > 0 and count > self.__limit:
                break
        return result