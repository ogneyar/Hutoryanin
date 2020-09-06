import json


class CallbackGame:
    'класс типов телеграм объектов'


    def __init__(self, obj):
        return True


    def get(self):
        response = {}
        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())
