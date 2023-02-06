from actions.base_action import BaseAction

class NextVersionAction(BaseAction):
    def __init__(self, config_filename):
        BaseAction.__init__(self, config_filename)

    def run(self):
        messages = self.git.get_messages()
        versions = self.git.get_versions()

        current_key = None
        current_version = self.semver.get_version()
        if len(versions) > 0:
            current_key = list(versions.keys())[0]
            current_version = self.semver.parse_version(versions[current_key])

        new_messages = {}
        saw_current_version = False
        for key in reversed(messages.keys()):
            if key == current_key:
                saw_current_version = True
                continue
            if not saw_current_version:
                continue
            saw_current_version = True
            new_messages[key] = messages[key]

        have_major = False
        have_minor = False
        for key in new_messages.keys():
            if self.convention.is_major(new_messages[key]):
                have_major = True
            elif self.convention.is_minor(new_messages[key]):
                have_minor = True

        next_version = current_version
        if have_major:
            next_version['major'] = next_version['major'] + 1
            next_version['minor'] = 0
            next_version['patch'] = 0
        elif have_minor:
            next_version['minor'] = next_version['minor'] + 1
            next_version['patch'] = 0
        else:
            next_version['patch'] = next_version['patch'] + 1

        next_version_str = self.semver.stringify_version(next_version)
        return next_version_str
