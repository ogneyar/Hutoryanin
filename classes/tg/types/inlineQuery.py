class InlineQuery:
    'класс типов телеграм объектов'

    #	String	Unique identifier for this query
    id = ""
    #	User	Sender
    from_user = None

    #	Location	Optional. Sender location, only for bots that request user location
    location = None

    #	String	Text of the query (up to 256 characters)
    query = ""
    #	String	Offset of the results to be returned, can be controlled by the bot
    offset = ""



    def __init__(self, obj):
        self.setId(obj['id'])
        self.setFrom(obj['from'])

        if 'location' in obj:
            self.setLocation(obj['location'])

        self.setQuery(obj['query'])
        self.setOffset(obj['offset'])


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
    def setQuery(self, val):
        self.query = val

    # получение
    def getQuery(self):
        return self.query


    # запись
    def setOffset(self, val):
        self.offset = val

    # получение
    def getOffset(self):
        return self.offset



