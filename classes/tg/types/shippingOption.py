class ShippingOption:
    'класс типов телеграм объектов'

    #	String	Shipping option identifier
    id = ""
    #	String	Option title
    title = ""
    #	Array of LabeledPrice	List of price portions
    prices = []


    def __init__(self, obj):
        self.setId(obj['id'])
        self.setTitle(obj['title'])
        self.setPrices(obj['prices'])


    # запись
    def setId(self, val):
        self.id = val

    # получение
    def getId(self):
        return self.id


    # запись
    def setTitle(self, val):
        self.title = val

    # получение
    def getTitle(self):
        return self.title


    # запись
    def setPrices(self, val):
        self.prices = val

    # получение
    def getPrices(self):
        return self.prices



