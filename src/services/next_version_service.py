from src.core.semver import Semver
from src.core.convention import Convention

class NextVersionService:
    def __init__(self, cfg):
        self.__semver = Semver(cfg)
        self.__convention = Convention(cfg)

    def run(self, messages, versions):
        current_key = None
        current_version = self.__semver.get_version()
        if len(versions) > 0:
            current_key = versions[0]['hash']
            current_version = self.__semver.parse_version(versions[0]['value'])

        new_messages = []
        saw_current_version = False if current_key != None else True
        for message in reversed(messages):
            key = message['hash']
            if key == current_key:
                saw_current_version = True
                continue
            if not saw_current_version:
                continue
            saw_current_version = True
            new_messages.append(message)

        have_major = False
        have_minor = False
        have_patch = False
        for message in new_messages:
            if self.__convention.is_major(message['value']):
                have_major = True
            elif self.__convention.is_minor(message['value']):
                have_minor = True
            elif self.__convention.is_patch(message['value']):
                have_patch = True

        next_version = current_version
        if have_major:
            next_version['major'] = next_version['major'] + 1
            next_version['minor'] = 0
            next_version['patch'] = 0
        elif have_minor:
            next_version['minor'] = next_version['minor'] + 1
            next_version['patch'] = 0
        elif have_patch:
            next_version['patch'] = next_version['patch'] + 1

        next_version_str = self.__semver.stringify_version(next_version)
        return next_version_str