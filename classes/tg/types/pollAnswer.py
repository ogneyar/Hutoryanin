class PollAnswer:
    'класс типов телеграм объектов'

    # String	Unique poll identifier
    poll_id = ""
    # объект класса User	The user, who changed the answer to the poll
    user = None
    # Array of Integer	0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
    option_ids = []

    def __init__(self, obj):
        self.setPollId(obj['poll_id'])
        self.setUser(obj['user'])
        self.setOptionIds(obj['option_ids'])


    def setPollId(self, val):
        self.poll_id = val

    def getPollId(self):
        return self.poll_id


    def setUser(self, val):
        self.user = User(val)

    def getUser(self):
        return self.user


    def setOptionIds(self, val):
        self.option_ids = []
        self.option_ids = [val]

    def getOptionIds(self):
        return self.option_ids


