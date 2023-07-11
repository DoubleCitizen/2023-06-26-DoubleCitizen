import json


class ReaderJSON:
    def __init__(self, path):
        self.path = path

    # def read(self, encod=None):
    #     with open(self.path, 'r', encoding=encod) as file:
    #         lines = file.readlines()
    #         last_line = lines[-6:-1]
    #     return last_line

    def read_all(self, encod=None):
        with open(self.path, 'r', encoding=encod) as file:
            lines = file.read()
            result = json.loads(lines)
        return result
