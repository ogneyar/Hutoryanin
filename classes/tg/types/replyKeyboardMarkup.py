from classes.tg.types.keyboardButton import KeyboardButton


class ReplyKeyboardMarkup:
    'класс типов телеграм объектов'

    #	Array of Array of KeyboardButton	Array of button rows, each represented by an Array of KeyboardButton objects
    keyboard = []

    #	Boolean	Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    resize_keyboard = False
    #	Boolean	Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
    one_time_keyboard = False
    #	Boolean	Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
    #Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
    selective = False


    def __init__(self, obj):
        self.setKeyboard(obj['keyboard'])

        if 'resize_keyboard' in obj:
            self.setResizeKeyboard(obj['resize_keyboard'])
        if 'one_time_keyboard' in obj:
            self.setOneTimeKeyboard(obj['one_time_keyboard'])
        if 'selective' in obj:
            self.setSelective(obj['selective'])


    # запись двумерного массива объектов класса KeyboardButton
    def setKeyboard(self, val):
        self.keyboard = []
        arr = []
        i = 0
        j = 0
        while i < len(val):
            while j < len(val[i]):
                arr.append(KeyboardButton(val[i][j]))
                j += 1
            self.keyboard.append(arr)
            j = 0
            i += 1
            arr = []

    # получение двумерного массива объектов класса KeyboardButton
    def getKeyboard(self):
        return self.keyboard


    # запись
    def setResizeKeyboard(self, val):
        self.resize_keyboard = val

    # получение
    def getResizeKeyboard(self):
        return self.resize_keyboard


    # запись
    def setOneTimeKeyboard(self, val):
        self.one_time_keyboard = val

    # получение
    def getOneTimeKeyboard(self):
        return self.one_time_keyboard


    # запись
    def setSelective(self, val):
        self.selective = val

    # получение
    def getSelective(self):
        return self.selective


