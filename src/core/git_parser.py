from core.semver import Semver

class GitParser:
    def __init__(self, cfg):
        self.cfg = cfg

    def parse_versions(self, tags):
        semver = Semver(self.cfg)
        result = {}
        lines = tags.split('\n')
        for i in range(0, len(lines)):
            line = lines[i][1:-1]
            key = line[:7]
            val = line[8:]
            version = semver.parse_version(val)
            if version != None:
                result[key] = semver.stringify_version(version)
        return result

    def parse_messages(self, messages):
        result = {}
        lines = messages.split('\n')
        for i in range(0, len(lines)):
            line = lines[i][1:-1]
            key = line[:7]
            val = line[8:]
            result[key] = val
        return result
