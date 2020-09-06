class ResponseParameters:
    'класс типов телеграм объектов'

    #	Integer	Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    migrate_to_chat_id = 0
    #	Integer	Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    retry_after = 0


    def __init__(self, obj):
        if 'migrate_to_chat_id' in obj:
            self.setMigrateToChatId(obj['migrate_to_chat_id'])
        if 'retry_after' in obj:
            self.setRetryAfter(obj['retry_after'])


    # запись
    def setMigrateToChatId(self, val):
        self.migrate_to_chat_id = val

    # получение
    def getMigrateToChatId(self):
        return self.migrate_to_chat_id


    # запись
    def setRetryAfter(self, val):
        self.retry_after = val

    # получение
    def getRetryAfter(self):
        return self.retry_after


