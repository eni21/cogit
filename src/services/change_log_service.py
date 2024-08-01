class ChangeLogService:
    #
    # messages = [{'hash': '$hash', 'value':'$message'}...]
    # versions = [{'hash': '$hash', 'value':'$version'}...]
    #
    def run(self, messages, versions, limit=0):
        # print(f'limit={limit}')
        versionsDict = self.__get_dict(versions)
        current = 0
        lines = ''
        for message in messages:
            hash = message['hash']
            if hash in versionsDict or lines == '':
                current += 1
                if limit != 0 and current > limit:
                    break
            if hash in versionsDict:
                if lines != '':
                    lines += '\n'
                lines += versionsDict[hash] + '\n\n'
            elif lines == '':
                lines += '*new*\n\n'
            lines += '\t' + message['value'] + '\n'
        return lines
    
    def __get_dict(self, items):
        result = {}
        for item in items:
            key = item['hash']
            val = item['value']
            result[key] = val
        return result
