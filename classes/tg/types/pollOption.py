class PollOption:
    'класс типов телеграм объектов'

    #	String	Option text, 1-100 characters
    text = ""
    #	Integer	Number of users that voted for this option
    voter_count = 0


    def __init__(self, obj):
        self.setText(obj['text'])
        self.setVoterCount(obj['voter_count'])


    def setText(self, val):
        self.text = val

    def getText(self):
        return self.text


    def setVoterCount(self, val):
        self.voter_count = val

    def getVoterCount(self):
        return self.voter_count



