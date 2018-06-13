import os
import json


class Config(object):
    config_path = str()
    conf = dict()

    def __init__(self):
        current_path = os.path.abspath(__file__)
        father_path = os.path.abspath(os.path.dirname(os.path.dirname(current_path)) + os.path.sep + ".")
        self.config_path = os.path.join(father_path, "conf/")
        self.conf = self.read("conf.json")

    def read(self, file):
        file = self.config_path + file
        f = open(file)
        text = f.read()
        f.close()
        return json.loads(text)


conf = Config()
