from providers.config import Config
from providers.git import Git
from core.convention import Convention

class DebugConvention():
    def __init__(self, config_filename, limit):
        self.__config_filename = config_filename
        self.__limit = limit

    def run(self):
        cfg = Config(self.__config_filename).get_config()
        git = Git(cfg)
        convention = Convention(cfg)

        messages = git.get_messages()
        result = ''
        count = 0
        for item in messages:
            kind = '[nul]'
            if convention.is_major(item['value']):
                kind = 'major'
            elif convention.is_minor(item['value']):
                kind = 'minor'
            elif convention.is_patch(item['value']):
                kind = 'patch'
            result += f'{kind} => {item["hash"]} {item["value"]}\n'
            count += 1
            if self.__limit > 0 and count > self.__limit:
                break
        return result