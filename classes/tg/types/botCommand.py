class BotCommand:
    'класс типов телеграм объектов'

    #	String	Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    command = ""
    #	String	Description of the command, 3-256 characters.
    description = ""


    def __init__(self, obj):
        self.setCommand(obj['command'])
        self.setDescription(obj['description'])


    # запись
    def setCommand(self, val):
        self.command = val

    # получение
    def getCommand(self):
        return self.command


    # запись
    def setDescription(self, val):
        self.description = val

    # получение
    def getDescription(self):
        return self.description


