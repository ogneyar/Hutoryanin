from classes.tg.types.keyboardButtonPollType import KeyboardButtonPollType


class KeyboardButton:
    'класс типов телеграм объектов'

    #	String	Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
    text = ""

    #	Boolean	Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
    request_contact = False
    #	Boolean	Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only
    request_location = False
    # объект класса KeyboardButtonPollType	Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only
    request_poll = None


    def __init__(self, obj):
        self.setText(obj['text'])

        if 'request_contact' in obj:
            self.setRequestContact(obj['request_contact'])
        if 'request_location' in obj:
            self.setRequestLocation(obj['request_location'])
        if 'request_poll' in obj:
            self.setRequestPoll(obj['request_poll'])


    # запись
    def setText(self, val):
        self.text = Location(val)

    # получение
    def getText(self):
        return self.text


    # запись
    def setRequestContact(self, val):
        self.request_contact = val

    # получение
    def getRequestContact(self):
        return self.request_contact


    # запись
    def setRequestLocation(self, val):
        self.request_location = val

    # получение
    def getRequestLocation(self):
        return self.request_location


    # запись объекта класса KeyboardButtonPollType
    def setRequestPoll(self, val):
        self.request_poll = KeyboardButtonPollType(val)

    # получение объекта класса KeyboardButtonPollType
    def getRequestPoll(self):
        return self.request_poll



