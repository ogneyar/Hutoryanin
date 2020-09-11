class SuccessfulPayment:
    'класс типов телеграм объектов'

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

    #	String	Telegram payment identifier
    telegram_payment_charge_id = ""
    #	String	Provider payment identifier
    provider_payment_charge_id = ""


    def __init__(self, obj):
        self.setCurrency(obj['currency'])
        self.setTotalAmount(obj['total_amount'])
        self.setInvoicePayload(obj['invoice_payload'])

        if 'shipping_option_id' in obj:
            self.setShippingOptionId(obj['shipping_option_id'])
        if 'order_info' in obj:
            self.setOrderInfo(obj['order_info'])

        self.setTelegramPaymentChargeId(obj['telegram_payment_charge_id'])
        self.setProviderPaymentChargeId(obj['provider_payment_charge_id'])


    # запись id
    def setCurrency(self, val):
        self.currency = val

    # получение id
    def getCurrency(self):
        return self.currency


    # запись id
    def setTotalAmount(self, val):
        self.total_amount = val

    # получение id
    def getTotalAmount(self):
        return self.total_amount


    # запись id
    def setInvoicePayload(self, val):
        self.invoice_payload = val

    # получение id
    def getInvoicePayload(self):
        return self.invoice_payload


    # запись id
    def setShippingOptionId(self, val):
        self.shipping_option_id = val

    # получение id
    def getShippingOptionId(self):
        return self.shipping_option_id


    # запись id
    def setOrderInfo(self, val):
        self.order_info = val

    # получение id
    def getOrderInfo(self):
        return self.order_info


    # запись id
    def setProviderPaymentChargeId(self, val):
        self.telegram_payment_charge_id = val

    # получение id
    def getProviderPaymentChargeId(self):
        return self.telegram_payment_charge_id


    # запись id
    def setProviderPaymentChargeId(self, val):
        self.provider_payment_charge_id = val

    # получение id
    def getProviderPaymentChargeId(self):
        return self.provider_payment_charge_id



