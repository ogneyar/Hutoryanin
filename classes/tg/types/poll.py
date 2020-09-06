from classes.tg.types.pollOption import PollOption
from classes.tg.types.messageEntity import MessageEntity

import json



class Poll:
    'класс типов телеграм объектов'

    #	String	Unique poll identifier
    poll_id = ""
    #	String	Poll question, 1-255 characters
    question = ""
    #	Array of PollOption	List of poll options
    options = []
    #	Integer	Total number of users that voted in the poll
    total_voter_count = 0
    #	Boolean	True, if the poll is closed
    is_closed = False
    #	Boolean	True, if the poll is anonymous
    is_anonymous = False
    #	String	Poll type, currently can be “regular” or “quiz”
    type = ""
    #	Boolean	True, if the poll allows multiple answers
    allows_multiple_answers = False

    #	Integer	Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    correct_option_id = 0
    #	String	Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    explanation = ""
    #	Array of MessageEntity	Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    explanation_entities = []
    #	Integer	Optional. Amount of time in seconds the poll will be active after creation
    open_period = 0
    #	Integer	Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    close_date = 0


    def __init__(self, obj):
        self.setId(obj['id'])
        self.setQuestion(obj['question'])
        self.setOptions(obj['options'])
        self.setTotalVoterCount(obj['total_voter_count'])
        self.setIsClosed(obj['is_closed'])
        self.setIsAnonymous(obj['is_anonymous'])
        self.setType(obj['type'])
        self.setAllowsMultipleAnswers(obj['allows_multiple_answers'])

        if 'correct_option_id' in obj:
            self.setCorrectOption_id(obj['correct_option_id'])
        if 'explanation' in obj:
            self.setExplanation(obj['explanation'])
        if 'explanation_entities' in obj:
            self.setExplanationEntities(obj['explanation_entities'])
        if 'open_period' in obj:
            self.setOpenPeriod(obj['open_period'])
        if 'close_date' in obj:
            self.setCloseDate(obj['close_date'])


    def get(self):
        response = {
            'id':self.id,
            'question':self.question,
            'options':self.options,
            'total_voter_count':self.total_voter_count,
            'is_closed':self.is_closed,
            'is_anonymous':self.is_anonymous,
            'type':self.type,
            'allows_multiple_answers':self.allows_multiple_answers
        }

        if self.correct_option_id != 0:
            response.update({'correct_option_id':self.correct_option_id})
        if self.explanation != "":
            response.update({'explanation':self.explanation})
        if self.explanation_entities != []:
            explanation_ent = []
            i = 0
            while i < len(self.explanation_entities):
                explanation_ent.append(self.explanation_entities[i].get())
                i += 1
            response.update({'explanation_entities':explanation_ent})
        if self.open_period != 0:
            response.update({'open_period':self.open_period})
        if self.close_date != 0:
            response.update({'close_date':self.close_date})

        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    def setId(self, val):
        self.poll_id = val

    def getId(self):
        return self.poll_id


    def setQuestion(self, val):
        self.question = val

    def getQuestion(self):
        return self.question


    def setOptions(self, val):
        self.options = []
        i = 0
        while i < len(val):
            self.options.append(PollOption(val[i]))
            i += 1

    def getOptions(self):
        return self.options


    def setTotalVoterCount(self, val):
        self.total_voter_count = val

    def getTotalVoterCount(self):
        return self.total_voter_count


    def setIsClosed(self, val):
        self.is_closed = val

    def getIsClosed(self):
        return self.is_closed


    def setIsAnonymous(self, val):
        self.is_anonymous = val

    def getIsAnonymous(self):
        return self.is_anonymous


    def setType(self, val):
        self.type = val

    def getType(self):
        return self.type


    def setAllowsMultipleAnswers(self, val):
        self.allows_multiple_answers = val

    def getAllowsMultipleAnswers(self):
        return self.allows_multiple_answers


    def setCorrectOption_id(self, val):
        self.correct_option_id = val

    def getCorrectOption_id(self):
        return self.correct_option_id


    def setExplanation(self, val):
        self.explanation = val

    def getExplanation(self):
        return self.explanation


    def setExplanationEntities(self, val):
        self.explanation_entities = []
        i = 0
        while i < len(val):
            self.explanation_entities.append(MessageEntity(val[i]))
            i += 1

    def getExplanationEntities(self):
        return self.explanation_entities


    def setOpenPeriod(self, val):
        self.open_period = val

    def getOpenPeriod(self):
        return self.open_period


    def setCloseDate(self, val):
        self.close_date = val

    def getCloseDate(self):
        return self.close_date



