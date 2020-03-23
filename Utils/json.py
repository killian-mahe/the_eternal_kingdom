# -*- coding: utf-8 -*-
import json

class Json(object):

    def __init__(self, file_name):
        f = open(file_name)
        self.json = f.read()
        f.close()
        pass

    def load(self):
        self.__dict__ = json.loads(self.json) 