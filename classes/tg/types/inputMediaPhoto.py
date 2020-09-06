class InputMediaPhoto:
    'класс типов телеграм объектов'

    #	String	Type of the result, must be photo
    input_type = ""
    #	String	File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    media = ""

    #	String	Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    caption = ""
    #	String	Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    parse_mode = ""


    def __init__(self, obj):
        self.setType(obj['type'])
        self.setMedia(obj['media'])

        if 'caption' in obj:
            self.setCaption(obj['caption'])
        if 'parse_mode' in obj:
            self.setParseMode(obj['parse_mode'])


    # запись
    def setType(self, val):
        self.input_type = val

    # получение
    def getType(self):
        return self.input_type


    # запись
    def setMedia(self, val):
        self.media = val

    # получение
    def getMedia(self):
        return self.media


    # запись
    def setCaption(self, val):
        self.caption = val

    # получение
    def getCaption(self):
        return self.caption


    # запись
    def setParseMode(self, val):
        self.parse_mode = val

    # получение
    def getParseMode(self):
        return self.parse_mode



