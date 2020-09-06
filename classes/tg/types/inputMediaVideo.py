class InputMediaVideo:
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
    #	Integer	Optional. Video width
    width = 0
    #	Integer	Optional. Video height
    height = 0
    #	Integer	Optional. Video duration
    duration = 0
    #	Boolean	Optional. Pass True, if the uploaded video is suitable for streaming
    supports_streaming = False


    def __init__(self, obj):
        self.setType(obj['type'])
        self.setMedia(obj['media'])
        self.setThumb(obj['thumb'])

        if 'caption' in obj:
            self.setCaption(obj['caption'])
        if 'parse_mode' in obj:
            self.setParseMode(obj['parse_mode'])
        if 'width' in obj:
            self.setWidth(obj['width'])
        if 'height' in obj:
            self.setHeight(obj['height'])
        if 'duration' in obj:
            self.setDuration(obj['duration'])
        if 'supports_streaming' in obj:
            self.setSupportsStreaming(obj['supports_streaming'])


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


    # запись
    def setWidth(self, val):
        self.width = val

    # получение
    def getWidth(self):
        return self.width


    # запись
    def setHeight(self, val):
        self.height = val

    # получение
    def getHeight(self):
        return self.height


    # запись
    def setDuration(self, val):
        self.duration = val

    # получение
    def getDuration(self):
        return self.duration


    # запись
    def setSupportsStreaming(self, val):
        self.supports_streaming = val

    # получение
    def getSupportsStreaming(self):
        return self.supports_streaming





