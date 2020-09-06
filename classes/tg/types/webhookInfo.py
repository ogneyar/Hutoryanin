class WebhookInfo:
    'класс типов телеграм объектов'

    #	String	Webhook URL, may be empty if webhook is not set up
    url = ""
    #	Boolean	True, if a custom certificate was provided for webhook certificate checks
    has_custom_certificate = False
    #	Integer	Number of updates awaiting delivery
    pending_update_count = 0

    #	Integer	Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
    last_error_date = 0
    #	String	Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
    last_error_message = ""
    #	Integer	Optional. Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
    max_connections = 0
    #	Array of String	Optional. A list of update types the bot is subscribed to. Defaults to all update types
    allowed_updates = []

    def __init__(self, obj):
        self.setUrl(obj['url'])
        self.setHasCustomCertificate(obj['has_custom_certificate'])
        self.setPendingUpdateCount(obj['pending_update_count'])
        if 'last_error_date' in obj:
            self.setLastErrorDate(obj['last_error_date'])
        if 'last_error_message' in obj:
            self.setLastErrorMessage(obj['last_error_message'])
        if 'max_connections' in obj:
            self.setMaxConnections(obj['max_connections'])
        if 'allowed_updates' in obj:
            self.setAllowedUpdates(obj['allowed_updates'])


    # запись
    def setUrl(self, val):
        self.url = val

    # получение
    def getUrl(self):
        return self.url


    # запись
    def setHasCustomCertificate(self, val):
        self.has_custom_certificate = val

    # получение
    def getHasCustomCertificate(self):
        return self.has_custom_certificate


    # запись
    def setPendingUpdateCount(self, val):
        self.pending_update_count = val

    # получение
    def getPendingUpdateCount(self):
        return self.pending_update_count


    # запись
    def setLastErrorDate(self, val):
        self.last_error_date = val

    # получение
    def getLastErrorDate(self):
        return self.last_error_date


    # запись
    def setLastErrorMessage(self, val):
        self.last_error_message = val

    # получение
    def getLastErrorMessage(self):
        return self.last_error_message


    # запись
    def setMaxConnections(self, val):
        self.max_connections = val

    # получение
    def getMaxConnections(self):
        return self.max_connections


    # запись
    def setAllowedUpdates(self, val):
        self.allowed_updates = []
        self.allowed_updates = [val]

        '''
        for key in val:
            self.allowed_updates.append(key)
        '''

        '''
        i = 0
        while i < len(val):
            self.allowed_updates.append(val[i])
            i += 1
        '''

    # получение
    def getAllowedUpdates(self):
        return self.allowed_updates



