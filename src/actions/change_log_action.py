from actions.base_action import BaseAction

class ChangeLogAction(BaseAction):
    def __init__(self, config_filename):
        BaseAction.__init__(self, config_filename)
    
    def run(self):
        messages = self.git.get_messages()
        versions = self.git.get_versions()
        lines = ''
        for hash, message in messages.items():
            if (hash in versions):
                if (lines != ''):
                    lines += '\n'
                lines += versions[hash] + '\n\n'
            elif (lines == ''):
                lines += '*new*\n\n'
            lines += '\t' + message + '\n'
        return lines