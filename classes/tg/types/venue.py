class Venue:
    'класс типов телеграм объектов'

    # объект класса Location	Venue location
    location = None
    #	String	Name of the venue
    title = ""
    #	String	Address of the venue
    address = ""

    #	String	Optional. Foursquare identifier of the venue
    foursquare_id = ""
    #	String	Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    foursquare_type = ""


    def __init__(self, obj):
        self.setLocation(obj['location'])
        self.setTitle(obj['title'])
        self.setAddress(obj['address'])

        if 'foursquare_id' in obj:
            self.setFoursquareId(obj['foursquare_id'])
        if 'foursquare_type' in obj:
            self.setFoursquareType(obj['foursquare_type'])


    # запись объекта класса Location
    def setLocation(self, val):
        self.file_id = Location(val)

    # получение объекта класса Location
    def getLocation(self):
        return self.file_id


    # запись заголовка
    def setTitle(self, val):
        self.title = val

    # получение заголовка
    def gtTitle(self):
        return self.title


    # запись
    def setAddress(self, val):
        self.address = val

    # получение
    def getAddress(self):
        return self.address


    # запись
    def setFoursquareId(self, val):
        self.foursquare_id = val

    # получение
    def getFoursquareId(self):
        return self.foursquare_id


    # запись
    def setFoursquareType(self, val):
        self.foursquare_type = val

    # получение
    def getFoursquareType(self):
        return self.foursquare_type



