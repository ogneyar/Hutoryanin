from classes.tg.types.loginUrl import LoginUrl
from classes.tg.types.callbackGame import CallbackGame

import json


class InlineKeyboardButton:
    'класс типов телеграм объектов'

    # String	Label text on the button
    text = ""

    # String	Optional. HTTP or tg:// url to be opened when button is pressed
    url = ""
    # объект класса LoginUrl	Optional. An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
    login_url = None
    # String	Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    callback_data = ""
    # String	Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. Can be empty, in which case just the bot's username will be inserted.
    #Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    switch_inline_query = ""
    # String	Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's username will be inserted.
    #This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.
    switch_inline_query_current_chat = ""
    # объект класса CallbackGame	Optional. Description of the game that will be launched when the user presses the button.
    #NOTE: This type of button must always be the first button in the first row.
    callback_game = None
    # Boolean	Optional. Specify True, to send a Pay button.
    #NOTE: This type of button must always be the first button in the first row.
    pay = False


    def __init__(self, obj):
        self.setText(obj['text'])

        if 'url' in obj:
            self.setUrl(obj['url'])
        if 'login_url' in obj:
            self.setLoginUrl(obj['login_url'])
        if 'callback_data' in obj:
            self.setCallbackData(obj['callback_data'])
        if 'switch_inline_query' in obj:
            self.setSwitchInlineQuery(obj['switch_inline_query'])
        if 'switch_inline_query_current_chat' in obj:
            self.setSwitchInlineQueryCurrentChat(obj['switch_inline_query_current_chat'])
        if 'callback_game' in obj:
            self.setCallbackGame(obj['callback_game'])
        if 'pay' in obj:
            self.setPay(obj['pay'])


    def get(self):
        response = {
            'text':self.text
        }

        if self.url != "":
            response.update({'url':self.url})
        if self.login_url is not None:
            response.update({'login_url':self.login_url.get()})
        if self.callback_data != "":
            response.update({'callback_data':self.callback_data})
        if self.switch_inline_query != "":
            response.update({'switch_inline_query':self.switch_inline_query})
        if self.switch_inline_query_current_chat != "":
            response.update({'switch_inline_query_current_chat':self.switch_inline_query_current_chat})
        if self.callback_game is not None:
            response.update({'callback_game':self.callback_game.get()})
        if self.pay != False:
            response.update({'pay':self.pay})

        return response


    def getStr(self):
        return str(self.get())

    def getJson(self):
        return json.dumps(self.get())


    # запись
    def setText(self, val):
        self.text = val

    # получение
    def getText(self):
        return self.text


    # запись
    def setUrl(self, val):
        self.url = val

    # получение
    def getUrl(self):
        return self.url


    # запись объекта класса LoginUrl
    def setLoginUrl(self, val):
        self.login_url = LoginUrl(val)

    # получение объекта класса LoginUrl
    def getLoginUrl(self):
        return self.login_url


    # запись
    def setCallbackData(self, val):
        self.callback_data = val

    # получение
    def getCallbackData(self):
        return self.callback_data


    # запись
    def setSwitchInlineQuery(self, val):
        self.switch_inline_query = val

    # получение
    def getSwitchInlineQuery(self):
        return self.switch_inline_query


    # запись
    def setSwitchInlineQueryCurrentChat(self, val):
        self.switch_inline_query_current_chat = val

    # получение
    def getSwitchInlineQueryCurrentChat(self):
        return self.switch_inline_query_current_chat


    # запись объекта класса CallbackGame
    def setCallbackGame(self, val):
        self.callback_game = CallbackGame(val)

    # получение объекта класса CallbackGame
    def getCallbackGame(self):
        return self.callback_game


    # запись
    def setPay(self, val):
        self.pay = val

    # получение
    def getPay(self):
        return self.pay





