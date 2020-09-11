from classes.tg.types.shippingAddress import ShippingAddress


class ShippingQuery:
    'класс типов телеграм объектов'

    #	String	Unique query identifier
    id = ""
    #	User	User who sent the query
    from_user = None
    #	String	Bot specified invoice payload
    invoice_payload = ""
    #	ShippingAddress	User specified shipping address
    shipping_address = None


    def __init__(self, obj):
        self.setId(obj['id'])
        self.setFrom(obj['from'])
        self.setInvoicePayload(obj['invoice_payload'])
        self.setShippingAddress(obj['shipping_address'])


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
    def setInvoicePayload(self, val):
        self.invoice_payload = val

    # получение
    def getInvoicePayload(self):
        return self.invoice_payload


    # запись
    def setShippingAddress(self, val):
        self.shipping_address = ShippingAddress(val)

    # получение
    def getShippingAddress(self):
        return self.shipping_address


