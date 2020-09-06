class ForceReply:
    'класс типов телеграм объектов'

    #	True	Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
    force_reply = False

    #	Boolean	Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
    selective = False


    def __init__(self, obj):
        self.setForceReply(obj['force_reply'])

        if 'selective' in obj:
            self.setSelective(obj['selective'])


    # запись
    def setForceReply(self, val):
        self.force_reply = val

    # получение
    def getForceReply(self):
        return self.force_reply


    # запись
    def setSelective(self, val):
        self.selective = val

    # получение
    def getSelective(self):
        return self.selective


