from providers.config import Config
from providers.git import Git
from services.change_log_service import ChangeLogService

class ChangeLogAction():
    def __init__(self, config_filename, limit):
        self.__cfg = Config(config_filename).get_config()
        self.__git = Git(self.__cfg)
        self.__limit = limit
    
    def run(self):
        messages = self.__git.get_messages()
        versions = self.__git.get_versions()
        return ChangeLogService().run(messages, versions, self.__limit)
