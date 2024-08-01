from providers.config import Config
from providers.git import Git
from services.current_version_service import CurrentVersionService

class CurrentVersionAction():
    def __init__(self, config_filename):
        self.__cfg = Config(config_filename).get_config()
        self.__git = Git(self.__cfg)
    def run(self):
        versions = self.__git.get_versions()
        return CurrentVersionService(self.__cfg).run(versions)
