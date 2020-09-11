from classes.tg.types.orderInfo import OrderInfo


class PreCheckoutQuery:
    'класс типов телеграм объектов'

    #	String	Unique query identifier
    id = ""
    #	User	User who sent the query
    from_user = None
    #	String	Three-letter ISO 4217 currency code
    currency = ""
    #	Integer	Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    total_amount = 0
    #	String	Bot specified invoice payload
    invoice_payload = ""
    #	String	Optional. Identifier of the shipping option chosen by the user
    shipping_option_id = ""
    #	OrderInfo	Optional. Order info provided by the user
    order_info = None


    def __init__(self, obj):
        self.setId(obj['id'])
        self.setFrom(obj['from'])
        self.setCurrency(obj['currency'])
        self.setTotalAmount(obj['total_amount'])
        self.setInvoicePayload(obj['invoice_payload'])
        if 'shipping_option_id' in obj:
            self.setShippingOptionId(obj['shipping_option_id'])
        if 'order_info' in obj:
            self.setOrderInfo(obj['order_info'])


    # запись
    def setId(self, val):
        self.id = val

    # получение
    def getId(self):
        return self.id


    # запись
    def setFrom(self, val):
        self.from_user = User(val)

    # получение
    def getFrom(self):
        return self.from_user


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


    # запись
    def setInvoicePayload(self, val):
        self.invoice_payload = val

    # получение
    def getInvoicePayload(self):
        return self.invoice_payload


    # запись
    def setShippingOptionId(self, val):
        self.shipping_option_id = val

    # получение
    def getShippingOptionId(self):
        return self.shipping_option_id


    # запись
    def setOrderInfo(self, val):
        self.order_info = OrderInfo(val)

    # получение
    def getOrderInfo(self):
        return self.order_info




