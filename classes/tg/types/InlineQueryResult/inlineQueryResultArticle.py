#from classes.tg.types.inputMessageContent import InputMessageContent


class InlineQueryResultArticle:
    'класс типов телеграм объектов'

    #	String	Type of the result, must be article
    type = ""
    #	String	Unique identifier for this result, 1-64 Bytes
    id = 0
    #	String	Title of the result
    title  = ""
    #	InputMessageContent	Content of the message to be sent
    input_message_content = None

    #	InlineKeyboardMarkup	Optional. Inline keyboard attached to the message
    reply_markup = None
    #	String	Optional. URL of the result
    url = ""
    #	Boolean	Optional. Pass True, if you don't want the URL to be shown in the message
    hide_url = False
    #	String	Optional. Short description of the result
    description = ""
    #	String	Optional. Url of the thumbnail for the result
    thumb_url = ""
    #	Integer	Optional. Thumbnail width
    thumb_width = 0
    #	Integer	Optional. Thumbnail height
    thumb_height = 0


    def __init__(self, obj):
        self.setType(obj['type'])
        self.setId(obj['id'])
        self.setTitle(obj['title'])
        self.setInputMessageContent(obj['input_message_content'])

        if 'reply_markup' in obj:
            self.setReplyMarkup(obj['reply_markup'])
        if 'url' in obj:
            self.setUrl(obj['url'])
        if 'hide_url' in obj:
            self.setHideUrl(obj['hide_url'])
        if 'description' in obj:
            self.setDescription(obj['description'])
        if 'thumb_url' in obj:
            self.setThumbUrl(obj['thumb_url'])
        if 'thumb_width' in obj:
            self.setThumbWidth(obj['thumb_width'])
        if 'thumb_height' in obj:
            self.setThumbHeight(obj['thumb_height'])


    # запись
    def setType(self, val):
        self.type = val

    # получение
    def getType(self):
        return self.type


    # запись
    def setId(self, val):
        self.id = val

    # получение
    def getId(self):
        return self.id


    # запись
    def setTitle(self, val):
        self.title = User(val)

    # получение
    def getTitle(self):
        return self.title


    # запись объекта класса InputMessageContent
    def setInputMessageContent(self, val):
        self.input_message_content = val

    # получение объекта класса InputMessageContent
    def getInputMessageContent(self):
        return self.input_message_content


    # запись объекта класса
    def setReplyMarkup(self, val):
        self.reply_markup = val

    # получение объекта класса
    def getReplyMarkup(self):
        return self.reply_markup


    # запись
    def setUrl(self, val):
        self.url = val

    # получение
    def getUrl(self):
        return self.url


    # запись
    def setHideUrl(self, val):
        self.hide_url = val

    # получение
    def getHideUrl(self):
        return self.hide_url


    # запись
    def setDescription(self, val):
        self.description = val

    # получение
    def getDescription(self):
        return self.description


    # запись
    def setThumbUrl(self, val):
        self.thumb_url =val
    # получение
    def getThumbUrl(self):
        return self.thumb_url


    # запись
    def setThumbWidth(self, val):
        self.thumb_width = val

    # получение
    def getThumbWidth(self):
        return self.thumb_width


    # запись
    def setThumbHeight(self, val):
        self.thumb_height = val

    # получение
    def getThumbHeight(self):
        return self.thumb_height





