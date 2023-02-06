from actions.base_action import BaseAction

class CurrentVersionAction(BaseAction):
    def __init__(self, config_filename):
        BaseAction.__init__(self, config_filename)

    def run(self):
        versions = self.git.get_versions()
        current_version = self.semver.stringify_version(self.semver.get_version())
        if len(versions) > 0:
            key = list(versions.keys())[0]
            current_version = versions[key]
        return current_version
