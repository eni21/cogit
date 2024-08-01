from src.core.semver import Semver

class CurrentVersionService:
    def __init__(self, cfg):
        self.__semver = Semver(cfg)

    def run(self, versions):
        current_version = self.__semver.stringify_version(self.__semver.get_version())
        if len(versions) > 0:
            key = versions[0]['hash']
            current_version = versions[0]['value']
        return current_version