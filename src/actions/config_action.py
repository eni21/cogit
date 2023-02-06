from actions.base_action import BaseAction

class ConfigAction(BaseAction):
    def __init__(self, config_filename):
        BaseAction.__init__(self, config_filename)

    def run(self):
        return self.config
