from classes.tg.types.inlineKeyboardButton import InlineKeyboardButton

import json


class InlineKeyboardMarkup:
    'класс типов телеграм объектов'

    #	Array of Array of InlineKeyboardButton	Array of button rows, each represented by an Array of InlineKeyboardButton objects
    inline_keyboard = []


    def __init__(self, obj):
        self.setInlineKeyboard(obj['inline_keyboard'])


    def get(self):
        inline_key = []
        arr = []
        i = 0
        j = 0
        while i < len(self.inline_keyboard):
            while j < len(self.inline_keyboard[i]):
                arr.append(self.inline_keyboard[i][j].get())
                j += 1
            inline_key.append(arr)
            j = 0
            i += 1
            arr = []

        response = {
            'inline_keyboard':inline_key
        }

        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    # запись двумерного массива объектов класса InlineKeyboardButton
    def setInlineKeyboard(self, val):
        self.inline_keyboard = []
        arr = []
        i = 0
        j = 0
        while i < len(val):
            while j < len(val[i]):
                arr.append(InlineKeyboardButton(val[i][j]))
                j += 1
            self.inline_keyboard.append(arr)
            j = 0
            i += 1
            arr = []


    # получение двумерного массива объектов класса InlineKeyboardButton
    def getInlineKeyboard(self):
        return self.inline_keyboard


