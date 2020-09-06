class Location:
    'класс типов телеграм объектов'

    #	Float	Longitude as defined by sender
    longitude = 0
    #	Float	Latitude as defined by sender
    latitude = 0


    def __init__(self, obj):
        self.setLongitude(obj['longitude'])
        self.setLatitude(obj['latitude'])


    # запись
    def setLongitude(self, val):
        self.longitude = val

    # получение
    def getLongitude(self):
        return self.longitude


    # запись
    def setLatitude(self, val):
        self.latitude = val

    # получение
    def getLatitude(self):
        return self.latitude



