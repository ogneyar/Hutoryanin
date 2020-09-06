class User:
    'телеграм объект типа User'

    # Integer	Unique identifier for this user or bot
    id = 0
    # Boolean	True, if this user is a bot
    is_bot = False
    # String	User's or bot's first name
    first_name = ""

    # String	Optional. User's or bot's last name
    last_name = ""
    # String	Optional. User's or bot's username
    username = ""
    # String	Optional. IETF language tag of the user's language
    language_code = ""
    # Boolean	Optional. True, if the bot can be invited to groups. Returned only in getMe.
    can_join_groups = False
    # Boolean	Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
    can_read_all_group_messages = False
    # Boolean	Optional. True, if the bot supports inline queries. Returned only in getMe.
    supports_inline_queries = False


    # конструктор
    def __init__(self, obj):
        self.setId(obj['id'])
        self.setIsBot(obj['is_bot'])
        self.setFirstName(obj['first_name'])
        if 'last_name' in obj:
            self.setLastName(obj['last_name'])
        if 'username' in obj:
            self.setUserName(obj['username'])
        if 'language_code' in obj:
            self.setLanguageCode(obj['language_code'])
        if 'can_join_groups' in obj:
            self.setCanJoinGroups(obj['can_join_groups'])
        if 'can_read_all_group_messages' in obj:
            self.setCanReadAllGroupMessages(obj['can_read_all_group_messages'])
        if 'supports_inline_queries' in obj:
            self.setSupportsInlineQueries(obj['supports_inline_queries'])


    def get(self):
        response = {
            'id':self.id,
            'is_bot':self.is_bot,
            'first_name':self.first_name
        }
        
        if self.last_name != "":
            response.update({'last_name':self.last_name})
        
        if self.username != "":
            response.update({'username':self.username})
        if self.language_code != "":
            response.update({'language_code':self.language_code})
        if self.can_join_groups != False:
            response.update({'can_join_groups':self.can_join_groups})
        if self.can_read_all_group_messages != False:
            response.update({'can_read_all_group_messages':self.can_read_all_group_messages})
        if self.supports_inline_queries != False:
            response.update({'supports_inline_queries':self.supports_inline_queries})
        
        return response


    def setId(self, val):
        self.id = val

    def getId(self):
        return self.id


    def setIsBot(self, val):
        self.is_bot = val

    def getIsBot(self):
        return self.is_bot


    def setFirstName(self, val):
        self.first_name = val

    def getFirstName(self):
        return self.first_name


    def setLastName(self, val):
        self.last_name = val

    def getLastName(self):
        return self.last_name


    def setUserName(self, val):
        self.username = val

    def getUserName(self):
        return self.username


    def setLanguageCode(self, val):
        self.language_code = val

    def getLanguageCode(self):
        return self.language_code


    def setCanJoinGroups(self, val):
        self.can_join_groups = val

    def getCanJoinGroups(self):
        return self.can_join_groups


    def setCanReadAllGroupMessages(self, val):
        self.can_read_all_group_messages = val

    def getCanReadAllGroupMessages(self):
        return self.can_read_all_group_messages


    def setSupportsInlineQueries(self, val):
        self.supports_inline_queries = val

    def setSupportsInlineQueries(self):
        return self.supports_inline_queries


