import json


class LoginUrl:
    'класс типов телеграм объектов'

    #	String	An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.
    #NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
    url = ""

    #	String	Optional. New text of the button in forwarded messages.
    forward_text = ""
    #	String	Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
    bot_username = ""
    #	Boolean	Optional. Pass True to request the permission for your bot to send messages to the user.
    request_write_access = False


    def __init__(self, obj):
        self.setUrl(obj['url'])

        if 'forward_text' in obj:
            self.setForwardText(obj['forward_text'])
        if 'bot_username' in obj:
            self.setBotUsername(obj['bot_username'])
        if 'request_write_access' in obj:
            self.setRequestWriteAccess(obj['request_write_access'])


    def get(self):
        response = {
            'url':self.url
        }

        if self.forward_text != "":
            response.update({'forward_text':self.forward_text})
        if self.bot_username != "":
            response.update({'bot_username':self.bot_username})
        if self.request_write_access != False:
            response.update({'request_write_access':self.request_write_access})

        return response


    def getStr(self):
        return str(self.get())

    def getJson(self):
        return json.dumps(self.get())


    # запись
    def setUrl(self, val):
        self.url = val

    # получение
    def getUrl(self):
        return self.url


    # запись
    def setForwardText(self, val):
        self.forward_text = val

    # получение
    def getForwardText(self):
        return self.forward_text


    # запись
    def setBotUsername(self, val):
        self.bot_username = val

    # получение
    def getBotUsername(self):
        return self.bot_username


    # запись
    def setRequestWriteAccess(self, val):
        self.request_write_access = val

    # получение
    def getRequestWriteAccess(self):
        return self.request_write_access


