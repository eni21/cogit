import re

class Convention:
    def __init__(self, cfg):
        self.__major_re = re.compile(cfg['convention']['major'])
        self.__minor_re = re.compile(cfg['convention']['minor'])
        self.__patch_re = re.compile(cfg['convention']['patch'])

    def is_major(self, message):
        match = re.search(self.__major_re, message)
        return match != None
    
    def is_minor(self, message):
        match = re.search(self.__minor_re, message)
        return match != None

    def is_patch(self, message):
        match = re.search(self.__patch_re, message)
        return match != None
