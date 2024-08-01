import re
from core.semver import Semver

class GitParser:
    def __init__(self, cfg):
        self.__line_re = re.compile('^([^ $]+) ?([^$]+)$')
        self.__semver = Semver(cfg)

    def __parse_lines(self, input):
        result = []
        lines = input.split('\n')
        for i in range(0, len(lines)):
            line = lines[i][1:-1] # remove quotes in start and end of line
            if line == '':
                continue
            match = re.search(self.__line_re, line)
            if match == None:
                raise Exception(f'Can not parse line "{line}"')
            result.append({
                'hash': match[1],
                'value': match[2]})
        return result

    def parse_versions(self, tags):
        lines = self.__parse_lines(tags)
        result = []
        for item in lines:
            if item['value'] == None:
                continue
            version = self.__semver.parse_version(item['value'])
            if version != None:
                result.append({
                    'hash': item['hash'],
                    'value': self.__semver.stringify_version(version),
                })
        return result

    def parse_messages(self, messages):
        return self.__parse_lines(messages)
