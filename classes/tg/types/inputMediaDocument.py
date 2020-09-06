class InputMediaDocument:
    'класс типов телеграм объектов'

    #	String	Type of the result, must be video
    input_type = ""
    #	String	File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    media = ""
    #	InputFile or String	Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    thumb = ""

    #	String	Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    caption = ""
    #	String	Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    parse_mode = ""


    def __init__(self, obj):
        self.setType(obj['type'])
        self.setMedia(obj['media'])
        self.setThumb(obj['thumb'])

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
    def setThumb(self, val):
        self.thumb = val

    # получение
    def getThumb(self):
        return self.thumb


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



