import json


class Contact:
    'класс типов телеграм объектов'

    # String	Contact's phone number
    phone_number = ""
    # String	User's or bot's first name
    first_name = ""

    # String	Optional. User's or bot's last name
    last_name = ""
    # Integer  Optional. Unique identifier for this user or bot
    user_id = 0
    # String	Optional. Additional data about the contact in the form of a vCard
    vcard = ""


    def __init__(self):
        self.setPhoneNumber(obj['phone_number'])
        self.setFirstName(obj['first_name'])

        if 'last_name' in obj:
            self.setLastName(obj['last_name'])
        if 'user_id' in obj:
            self.setUserId(obj['user_id'])
        if 'vcard' in obj:
            self.setVcard(obj['vcard'])


    def get(self):
        response = {
            'phone_number':self.phone_number,
            'first_name':self.first_name
        }

        if self.last_name != "":
            response.update({'last_name':self.last_name})
        if self.user_id != 0:
            response.update({'user_id':self.user_id})
        if self.vcard != "":
            response.update({'vcard':self.vcard})

        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    def setPhoneNumber(self, val):
        self.phone_number = val

    def getPhoneNumber(self):
        return self.phone_number


    def setFirstName(self, val):
        self.first_name = val

    def getFirstName(self):
        return self.first_name


    def setLastName(self, val):
        self.last_name = val

    def getLastName(self):
        return self.last_name


    def setUserId(self, val):
        self.user_id = val

    def getUserId(self):
        return self.user_id


    def setVcard(self, val):
        self.vcard = val

    def getVcard(self):
        return self.vcard


