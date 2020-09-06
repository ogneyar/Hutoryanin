import json


class Dice:
    'класс типов телеграм объектов'

    #	String	Emoji on which the dice throw animation is based
    emoji = ""
    #	Integer	Value of the dice, 1-6 for “🎲” and “🎯” base emoji, 1-5 for “🏀” base emoji
    value = 0

    def __init__(self, obj):
        self.setEmoji(obj['emoji'])
        self.setValue(obj['value'])


    def get(self):
        response = {
            'emoji':self.emoji,
            'value':self.value
        }
        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    def setEmoji(self, val):
        self.emoji = val

    def getEmoji(self):
        return self.emoji


    def setValue(self, val):
        self.value = val

    def getValue(self):
        return self.value




