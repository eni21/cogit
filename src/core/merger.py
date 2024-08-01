class Merger:
    def merge_dicts(self, a, b):
        result = a.copy()
        for key in b:
            if not key in result:
                result[key] = b[key]
            if isinstance(result[key], dict) and isinstance(b[key], dict):
                result[key] = self.merge_dicts(result[key], b[key])
            else:
                result[key] = b[key]
        return result
