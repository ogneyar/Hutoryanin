# class Message подключен в update.py
from classes.tg.types.chatPhoto import ChatPhoto
from classes.tg.types.chatPermissions import ChatPermissions


class Chat:
    'телеграм объект типа Chat'

    # целочисленный тип данных int
    chat_id = 0
    # строковый тип данных str
    chat_type = ""

    # строковый тип данных str (Optional)
    title = ""
    # строковый тип данных str (Optional)
    username = ""
    # строковый тип данных str (Optional)
    first_name = ""
    # строковый тип данных str (Optional)
    last_name = ""
    # объект класса ChatPhoto (Optional)
    photo = None
    # строковый тип данных str (Optional)
    description = ""
    # строковый тип данных str (Optional)
    invite_link = ""
    # объект класса Message (Optional)
    pinned_message = None
    # объект класса ChatPermissions (Optional)
    permissions = None
    # целочисленный тип данных int (Optional)
    slow_mode_delay = 0
    # строковый тип данных str (Optional)
    sticker_set_name = ""
    # булевый тип данных bool (Optional)
    can_set_sticker_set = None


    # конструктор
    def __init__(self, obj):
        self.setId(obj['id'])
        self.setType(obj['type'])
        if 'title' in obj:
            self.setTitle(obj['title'])
        if 'username' in obj:
            self.setUsername(obj['username'])
        if 'first_name' in obj:
            self.setFirstName(obj['first_name'])
        if 'last_name' in obj:
            self.setLastName(obj['last_name'])
        if 'photo' in obj:
            self.setPhoto(obj['photo'])
        if 'description' in obj:
            self.setDescription(obj['description'])
        if 'invite_link' in obj:
            self.setInviteLink(obj['invite_link'])
        if 'pinned_message' in obj:
            self.setPinnedMessage(obj['pinned_message'])
        if 'permissions' in obj:
            self.setPermissions(obj['permissions'])
        if 'slow_mode_delay' in obj:
            self.setSlowModeDelay(obj['slow_mode_delay'])
        if 'sticker_set_name' in obj:
            self.setStickerSetName(obj['sticker_set_name'])
        if 'can_set_sticker_set' in obj:
            self.setCanSetStickerSet(obj['can_set_sticker_set'])


    def get(self):
        response = {
            'id':self.chat_id,
            'type':self.chat_type
        }
        
        if self.title != "":
            response.update({'title':self.title})
        if self.username != "":
            response.update({'username':self.username})
        if self.first_name != "":
            response.update({'first_name':self.first_name})
        if self.last_name != "":
            response.update({'last_name':self.last_name})
        if self.photo is not None:
            response.update({'photo':self.photo.get()})
        if self.description != "":
            response.update({'description':self.description})
        if self.invite_link != "":
            response.update({'invite_link':self.invite_link})
        if self.pinned_message is not None:
            response.update({'pinned_message':self.pinned_message.get()})
        if self.permissions is not None:
            response.update({'permissions':self.permissions.get()})
        if self.slow_mode_delay != 0:
            response.update({'slow_mode_delay':self.slow_mode_delay})
        if self.sticker_set_name != "":
            response.update({'sticker_set_name':self.sticker_set_name})
        if self.can_set_sticker_set is not None:
            response.update({'can_set_sticker_set':self.can_set_sticker_set})
        
        return response


    # запись id чата
    def setId(self, chatId):
        self.chat_id = chatId

    # получение id чата
    def getId(self):
        return self.chat_id


    # запись типа чата
    def setType(self, chatType):
        self.chat_type = chatType

    # получение типа чата
    def getType(self):
        return self.chat_type


    # запись заголовка
    def setTitle(self, ttl):
        self.title = ttl

    # получение заголовка
    def getTitle(self):
        return self.title


    # запись имени пользователя
    def setUsername(self, usrName):
        self.username = usrName

    # получение имени пользователя
    def getUsername(self):
        return self.username


    # запись первого имени
    def setFirstName(self, frstName):
        self.first_name = frstName

    # получение первого имени
    def getFirstName(self):
        return self.first_name


    # запись отчества
    def setLastName(self, lstName):
        self.last_name = lstName

    # получение отчества
    def getLastName(self):
        return self.last_name


    # запись объекта класса ChatPhoto
    def setPhoto(self, val):
        self.photo = ChatPhoto(val)

    # получение объекта класса ChatPhoto
    def getPhoto(self):
        return self.photo


    # запись описания
    def setDescription(self, val):
        self.description = val

    # получение описания
    def getDescription(self):
        return self.description


    # запись ссылки на приглошение
    def setInviteLink(self, val):
        self.invite_link = val

    # получение ссылки на приглошение
    def getInviteLink(self):
        return self.invite_link


    # запись объекта класса Message (закреплёное сообщение)
    def setPinnedMessage(self, val):
        from classes.tg.types.message import Message
        self.pinned_message = Message(val)

    # получение объекта класса Message (закреплёное сообщение)
    def getPinnedMessage(self):
        return self.pinned_message


    # запись объекта класса ChatPermissions (разрешения)
    def setPermissions(self, obj):
        self.permissions = ChatPermissions()
        self.permissions.set(
            obj['can_send_messages'],
            obj['can_send_media_messages'],
            obj['can_send_polls'],
            obj['can_send_other_messages'],
            obj['can_add_web_page_previews'],
            obj['can_change_info'],
            obj['can_invite_users'],
            obj['can_pin_messages'])

    # получение объекта класса ChatPermissions (разрешения)
    def getPermissions(self):
        return self.permissions


    # запись медленного режима задержки
    def setSlowModeDelay(self, val):
        self.slow_mode_delay = val

    # получение медленного режима задержки
    def getSlowModeDelay(self):
        return self.slow_mode_delay


    # запись имени стикера
    def setStickerSetName(self, val):
        self.sticker_set_name = val

    # получение имени стикера
    def getStickerSetName(self):
        return self.sticker_set_name


    # запись возможности установить набор наклеек
    def setCanSetStickerSet(self, val):
        self.can_set_sticker_set = val

    # получение возможности установить набор наклеек
    def getCanSetStickerSet(self):
        return self.can_set_sticker_set


