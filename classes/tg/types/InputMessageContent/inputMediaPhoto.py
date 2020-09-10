class InputTextMessageContent:
    'класс типов телеграм объектов'

    #	String	Text of the message to be sent, 1-4096 characters
    message_text = ""

    #	String	Optional. Mode for parsing entities in the message text. See formatting options for more details.
    parse_mode = ""
    #	Boolean	Optional. Disables link previews for links in the sent message
    disable_web_page_preview = False


    def __init__(self, obj):
        self.setMessageText(obj['message_text'])

        if 'parse_mode' in obj:
            self.setParseMode(obj['parse_mode'])
        if 'disable_web_page_preview' in obj:
            self.setDisableWebPagePreview(obj['disable_web_page_preview'])


    # запись
    def setMessageText(self, val):
        self.message_text = val

    # получение
    def getMessageText(self):
        return self.message_text


    # запись
    def setParseMode(self, val):
        self.parse_mode = val

    # получение
    def getParseMode(self):
        return self.parse_mode


    # запись
    def setDisableWebPagePreview(self, val):
        self.disable_web_page_preview = val

    # получение
    def getDisableWebPagePreview(self):
        return self.disable_web_page_preview




