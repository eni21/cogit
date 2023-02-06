import subprocess
from core.git_parser import GitParser

class Git:
    def __init__(self, cfg):
        self.cfg = cfg
        self.parser = GitParser(cfg)

    def get_versions(self):
        bytes = subprocess.check_output(['git', 'log', '--format="%h %d"', self.cfg['branch']], cwd=self.cfg['cwd'])
        string = bytes.decode('utf-8')
        versions = self.parser.parse_versions(string)
        return versions
    
    def get_messages(self):
        bytes = subprocess.check_output(['git', 'log', '--format="%h %s"', self.cfg['branch']], cwd=self.cfg['cwd'])
        string = bytes.decode('utf-8')
        messages = self.parser.parse_messages(string)
        return messages
