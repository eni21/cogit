from core.config import Config
from core.git import Git
from core.semver import Semver
from core.convention import Convention
from core.bumper import Bumper

class BaseAction:
    def __init__(self, config_filename):
        cfg = Config(config_filename)
        self.config = cfg.get_config()
        self.git = Git(self.config)
        self.semver = Semver(self.config)
        self.convention = Convention(self.config)
        self.bumper = Bumper(self.config)
