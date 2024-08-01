import subprocess
from core.git_parser import GitParser

class Git:
    def __init__(self, cfg):
        self.cfg = cfg
        self.parser = GitParser(cfg)

    def get_messages_raw(self):
        bytes = subprocess.check_output(['git', 'log', '--format="%h %s"', self.cfg['branch']], cwd=self.cfg['cwd'])
        return bytes.decode('utf-8')

    def get_versions_raw(self):
        bytes = subprocess.check_output(['git', 'log', '--format="%h %d"', self.cfg['branch']], cwd=self.cfg['cwd'])
        return bytes.decode('utf-8')

    def get_versions(self):
        string = self.get_versions_raw()
        versions = self.parser.parse_versions(string)
        return versions
    
    def get_messages(self):
        string = self.get_messages_raw()
        messages = self.parser.parse_messages(string)
        return messages
