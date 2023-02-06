import re

class Convention:
    def __init__(self, cfg):
        self.cfg = cfg

    def is_major(self, message):
        match = re.search(r'^[a-zA-Z0-9]!:', message)
        return match != None
    
    def is_minor(self, message):
        match = re.search(r'^feat:', message)
        return match != None
