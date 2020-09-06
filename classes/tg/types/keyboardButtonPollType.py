class KeyboardButtonPollType:
    'класс типов телеграм объектов'

    # String	Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    key_type = ""


    def __init__(self, obj):
        if 'type' in obj:
            self.setType(obj['type'])


    def setType(self, val):
        self.key_type = val


    def getType(self):
        return self.key_type




