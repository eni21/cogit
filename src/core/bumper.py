import os
import re

class Bumper:
    def __init__(self, config):
        self.config = config

    def bump(self, filename, pattern, version):
        content = self.__read_file(filename)
        content = self.__replace_version(content, pattern, version)
        self.__write_file(filename, content)

    def __get_find(self, pattern):
        return re.sub(r'\{version\}', '.+', pattern)

    def __get_replace(self, pattern, version):
        return re.sub(r'\{version\}', version, pattern)

    def __replace_version(self, content, pattern, version):
        find = self.__get_find(pattern)
        replace = self.__get_replace(pattern, version)
        lines = content.split('\n')
        result = ''
        for line in lines:
            match = re.search(find, line)
            if result != '':
                result += '\n'
            if  match == None:
                result += line
            else:
                result += replace
        return result

    def __read_file(self, filename):
        if os.path.isfile(filename):
            f = open(filename, 'r', encoding='utf-8')
            content = f.read()
            f.close()
            return content
        else:
            return ''

    def __write_file(self, filename, content):
        file = open(filename, 'w', encoding='utf-8')
        file.write(content)
        file.close()
