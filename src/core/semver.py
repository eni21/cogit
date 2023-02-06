import re

class Semver:
    def __init__(self, cfg):
        self.cfg = cfg
        self.pattern_re = self.__get_pattern_re()

    def __get_pattern_re(self):
        pattern = self.cfg['pattern']
        pattern = re.sub(r'\{major\}|\{minor\}|\{patch\}', '([0-9]+)', pattern)
        pattern = re.sub(r'\.', '\.', pattern)
        return pattern

    def get_version(self, major=0, minor=0, patch=0):
        return {
            'major': int(major),
            'minor': int(minor),
            'patch': int(patch),
        }

    def stringify_version(self, version):
        pattern = self.cfg['pattern']
        pattern = re.sub(r'\{major\}', str(version['major']), pattern)
        pattern = re.sub(r'\{minor\}', str(version['minor']), pattern)
        pattern = re.sub(r'\{patch\}', str(version['patch']), pattern)
        return pattern

    def parse_version(self, string):
        match = re.search(self.pattern_re, string)
        if match == None:
            return None
        return {
            'major': int(match.group(1)),
            'minor': int(match.group(2)),
            'patch': int(match.group(3)),
        }