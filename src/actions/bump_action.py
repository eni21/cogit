from actions.base_action import BaseAction

class BumpAction(BaseAction):
    def __init__(self, config_filename, version_str):
        BaseAction.__init__(self, config_filename)
        self.__version_str = version_str

    def run(self):
        for item in self.config['bump']:
            self.bumper.bump(item['filename'], item['pattern'], self.__version_str)
