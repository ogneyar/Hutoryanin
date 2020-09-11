class Invoice:
    'класс типов телеграм объектов'

    #	String	Product name
    title = ""
    #	String	Product description
    description = ""
    #	String	Unique bot deep-linking parameter that can be used to generate this invoice
    start_parameter = ""
    #	String	Three-letter ISO 4217 currency code
    currency = ""
    #	Integer	Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    total_amount = 0


    def __init__(self, obj):
        self.setTitle(obj['title'])
        self.setDescription(obj['description'])
        self.setStartParameter(obj['start_parameter'])
        self.setCurrency(obj['currency'])
        self.setTotalAmount(obj['total_amount'])


    # запись
    def setTitle(self, val):
        self.title = val

    # получение
    def getTitle(self):
        return self.title


    # запись
    def setDescription(self, val):
        self.description = val

    # получение
    def getDescription(self):
        return self.description


    # запись
    def setStartParameter(self, val):
        self.start_parameter = val

    # получение
    def getStartParameter(self):
        return self.start_parameter


    # запись
    def setCurrency(self, val):
        self.currency = val

    # получение
    def getCurrency(self):
        return self.currency


    # запись
    def setTotalAmount(self, val):
        self.total_amount = val

    # получение
    def getTotalAmount(self):
        return self.total_amount





