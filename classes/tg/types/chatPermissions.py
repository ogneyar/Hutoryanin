import json


class ChatPermissions:
    'класс типов телеграм объектов'

    #	Boolean	Optional. True, if the user is allowed to send text messages, contacts, locations and venues
    can_send_messages = False
    #	Boolean	Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
    can_send_media_messages = False
    #	Boolean	Optional. True, if the user is allowed to send polls, implies can_send_messages
    can_send_polls = False
    #	Boolean	Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
    can_send_other_messages = False
    #	Boolean	Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
    can_add_web_page_previews = False
    #	Boolean	Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
    can_change_info = False
    #	Boolean	Optional. True, if the user is allowed to invite new users to the chat
    can_invite_users = False
    #	Boolean	Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
    can_pin_messages = False


    def __init__(self, obj = None):
        if obj is not None:
            if 'can_send_messages' in obj:
                self.setCanSendMessages(obj['can_send_messages'])
            if 'can_send_media_messages' in obj:
                self.setCanSendMediaMessages(obj['can_send_media_messages'])
            if 'can_send_polls' in obj:
                self.setCanSendPolls(obj['can_send_polls'])
            if 'can_send_other_messages' in obj:
                self.setCanSendOtherMessages(obj['can_send_other_messages'])
            if 'can_add_web_page_previews' in obj:
                self.setCanAddWebPagePreviews(obj['can_add_web_page_previews'])
            if 'can_change_info' in obj:
                self.setCanChangeInfo(obj['can_change_info'])
            if 'can_invite_users' in obj:
                self.setCanInviteUsers(obj['can_invite_users'])
            if 'can_pin_messages' in obj:
                self.setCanPinMessages(obj['can_pin_messages'])


    def set(self,
            can_send_messages = False,
            can_send_media_messages = False,
            can_send_polls = False,
            can_send_other_messages = False,
            can_add_web_page_previews = False,
            can_change_info = False,
            can_invite_users = False,
            can_pin_messages = False):
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages


    def get(self): # dict
        response = {
            'can_send_messages':self.can_send_messages,
            'can_send_media_messages':self.can_send_media_messages,
            'can_send_polls':self.can_send_polls,
            'can_send_other_messages':self.can_send_other_messages,
            'can_add_web_page_previews':self.can_add_web_page_previews,
            'can_change_info':self.can_change_info,
            'can_invite_users':self.can_invite_users,
            'can_pin_messages':self.can_pin_messages
        }
        return response


    def getJson(self): # json
        response = self.get()
        return json.dumps(response)


    # запись возможности писать сообщения
    def setCanSendMessages(self, val):
        self.can_send_messages = val

    # получение возможности писать сообщения
    def getCanSendMessages(self):
        return self.can_send_messages


    # запись возможности отправлять медиа сообщения
    def setCanSendMediaMessages(self, val):
        self.can_send_media_messages = val

    # получение возможности отправлять медиа сообщения
    def getCanSendMediaMessages(self):
        return self.can_send_media_messages


    # запись возможности создавать опрос
    def setCanSendPolls(self, val):
        self.can_send_polls = val

    # получение возможности создавать опрос
    def getCanSendPolls(self):
        return self.can_send_polls


    # запись возможности отправлять другие сообщения
    def setCanSendOtherMessages(self, val):
        self.can_send_other_messages = val

    # получение возможности отправлять другие сообщения
    def setCanSendOtherMessages(self):
        return self.can_send_other_messages


    # запись возможности добавлять "превью" веб страниц
    def setCanAddWebPagePreviews(self, val):
        self.can_add_web_page_previews = val

    # получение возможности добавлять "превью" веб страниц
    def getCanAddWebPagePreviews(self):
        return self.can_add_web_page_previews


    # запись возможности менять информацию
    def setCanChangeInfo(self, val):
        self.can_change_info = val

    # получение возможности менять информацию
    def getCanChangeInfo(self):
        return self.can_change_info


    # запись возможности приглашать пользователей
    def setCanInviteUsers(self, val):
        self.can_invite_users = val

    # получение возможности приглашать пользователей
    def getCanInviteUsers(self):
        return self.can_invite_users


    # запись возможности закреплять сообщения
    def setCanPinMessages(self, val):
        self.can_pin_messages = val

    # получение возможности закреплять сообщения
    def setCanPinMessages(self):
        return self.can_pin_messages


