from providers.config import Config
from providers.git import Git
from services.next_version_service import NextVersionService

class NextVersionAction():
    def __init__(self, config_filename):
        self.__cfg = Config(config_filename).get_config()
        self.__git = Git(self.__cfg)

    def run(self):
        messages = self.__git.get_messages()
        versions = self.__git.get_versions()
        return NextVersionService(self.__cfg).run(messages, versions)
