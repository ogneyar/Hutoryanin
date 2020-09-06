from classes.tg.types.user import User

import json


class MessageEntity:
    'класс типов телеграм объектов'

    # String	Type of the entity. Can be “mention” (@username), “hashtag” (#hashtag), “cashtag” ($USD), “bot_command” (/start@jobs_bot), “url” (https://telegram.org), “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123), “bold” (bold text), “italic” (italic text), “underline” (underlined text), “strikethrough” (strikethrough text), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames)
    type = ""
    # Integer	Offset in UTF-16 code units to the start of the entity
    offset = 0
    # Integer	Length of the entity in UTF-16 code units
    length = 0

    # String	Optional. For “text_link” only, url that will be opened after user taps on the text
    url = ""
    # объект класса User	Optional. For “text_mention” only, the mentioned user
    user = None
    # String	Optional. For “pre” only, the programming language of the entity text
    language = ""


    def __init__(self, obj):
        self.setType(obj['type'])
        self.setOffset(obj['offset'])
        self.setLength(obj['length'])

        if 'url' in obj:
            self.setUrl(obj['url'])
        if 'user' in obj:
            self.setUser(obj['user'])
        if 'language' in obj:
            self.setLanguage(obj['language'])


    def get(self):
        response = {
            'type':self.type,
            'offset':self.offset,
            'length':self.length
        }

        if self.url != "":
            response.update({'url':self.url})
        if self.user is not None:
            response.update({'user':self.user.get()})
        if self.language != "":
            response.update({'language':self.language})

        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    #
    def setType(self, val):
        self.type = val

    def getType(self):
        return self.type


    #
    def setOffset(self, val):
        self.offset = val

    def getOffset(self):
        return self.offset


    #
    def setLength(self, val):
        self.length = val

    def getLength(self):
        return self.length



    #
    def setUrl(self, val):
        self.url = val

    def getUrl(self):
        return self.url


    #
    def setUser(self, val):
        self.user = User(val)

    def getUser(self):
        return self.user


    #
    def setLanguage(self, val):
        self.language = val

    def getLanguage(self):
        return self.language


