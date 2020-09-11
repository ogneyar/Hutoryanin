from classes.tg.types.shippingAddress import ShippingAddress


class OrderInfo:
    'класс типов телеграм объектов'

    #	String	Optional. User name
    name = ""
    #	String	Optional. User's phone number
    phone_number = ""
    #	String	Optional. User email
    email = ""
    #	ShippingAddress	Optional. User shipping address
    shipping_address = ""


    def __init__(self, obj):
        if 'name' in obj:
            self.setName(obj['name'])
        if 'phone_number' in obj:
            self.setPhoneNumber(obj['phone_number'])
        if 'email' in obj:
            self.setEmail(obj['email'])
        if 'shipping_address' in obj:
            self.setShippingAddress(obj['shipping_address'])


    # запись
    def setName(self, val):
        self.name = val

    # получение
    def getName(self):
        return self.name


    # запись
    def setPhoneNumber(self, val):
        self.phone_number = val

    # получение
    def getPhoneNumber(self):
        return self.phone_number


    # запись
    def setEmail(self, val):
        self.email = val

    # получение
    def getEmail(self):
        return self.email


    # запись
    def setShippingAddress(self, val):
        self.shipping_address = ShippingAddress(val)

    # получение
    def getShippingAddress(self):
        return self.shipping_address



