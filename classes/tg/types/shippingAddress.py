class ShippingAddress:
    'класс типов телеграм объектов'

    #	String	ISO 3166-1 alpha-2 country code
    country_code = ""
    #	String	State, if applicable
    state = ""
    #	String	City
    city = ""
    #	String	First line for the address
    street_line1 = ""
    #	String	Second line for the address
    street_line2 = ""
    #	String	Address post code
    post_code = ""


    def __init__(self, obj):
        self.setCountryCode(obj['country_code'])
        self.setState(obj['state'])
        self.setCity(obj['city'])
        self.setStreetLine1(obj['street_line1'])
        self.setStreetLine2(obj['street_line2'])
        self.setPostCode(obj['post_code'])


    # запись
    def setCountryCode(self, val):
        self.country_code = val

    # получение
    def getCountryCode(self):
        return self.country_code


    # запись
    def setState(self, val):
        self.state = val

    # получение
    def getState(self):
        return self.state


    # запись
    def setCity(self, val):
        self.city = val

    # получение
    def getCity(self):
        return self.city


    # запись
    def setStreetLine1(self, val):
        self.street_line1 = val

    # получение
    def getStreetLine1(self):
        return self.street_line1


    # запись
    def setStreetLine2(self, val):
        self.street_line2 = val

    # получение
    def getStreetLine2(self):
        return self.street_line2


    # запись
    def setPostCode(self, val):
        self.post_code = val

    # получение
    def getPostCode(self):
        return self.post_code


