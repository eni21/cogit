from src.io.config import Config
from src.io.git import Git

class DebugGitVersions():
    def __init__(self, config_filename, limit):
        cfg = Config(config_filename).get_config()
        self.__git = Git(cfg)
        self.__limit = limit

    def run(self):
        versions = self.__git.get_versions()
        return self.__print(versions)

    def __print(self, versions):
        result = []
        count = 0
        for item in versions:
            result.append(item)
            count += 1
            if self.__limit > 0 and count > self.__limit:
                break
        return result
