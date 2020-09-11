class LabeledPrice:
    'класс типов телеграм объектов'

    #	String	Portion label
    label = ""
    #	Integer	Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    amount = 0


    def __init__(self, obj):
        self.setLabel(obj['label'])
        self.setAmount(obj['amount'])


    # запись
    def setLabel(self, val):
        self.label = val

    # получение
    def getLabel(self):
        return self.label


    # запись
    def setAmount(self, val):
        self.amount = val

    # получение
    def getAmount(self):
        return self.amount


