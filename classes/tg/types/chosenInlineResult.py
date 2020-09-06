class ChosenInlineResult:
    'класс типов телеграм объектов'

    #	String	The unique identifier for the result that was chosen
    result_id = ""
    #	User	The user that chose the result
    from_user = None

    #	Location	Optional. Sender location, only for bots that require user location
    location = None
    #	String	Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
    inline_message_id = ""

    #	String	The query that was used to obtain the result
    query = ""



    def __init__(self, obj):
        self.setResultId(obj['result_id'])
        self.setFrom(obj['from'])

        if 'location' in obj:
            self.setLocation(obj['location'])
        if 'inline_message_id' in obj:
            self.setInlineMessageId(obj['inline_message_id'])

        self.setQuery(obj['query'])


    # запись
    def setId(self, val):
        self.id = val

    # получение
    def getId(self):
        return self.id


    # запись
    def setFrom(self, val):
        self.from_user = User(val)

    # получение
    def getFrom(self):
        return self.from_user


    # запись объекта класса Location
    def setLocation(self, val):
        self.file_id = Location(val)

    # получение объекта класса Location
    def getLocation(self):
        return self.file_id


    # запись
    def setInlineMessageId(self, val):
        self.inline_message_id = val

    # получение
    def getInlineMessageId(self):
        return self.inline_message_id


    # запись
    def setQuery(self, val):
        self.query = val

    # получение
    def getQuery(self):
        return self.query




