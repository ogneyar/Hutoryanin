class ChatMember:
    'класс типов телеграм объектов'

    #	User	Information about the user
    user = None
    #	String	The member's status in the chat. Can be “creator”, “administrator”, “member”, “restricted”, “left” or “kicked”
    status = ""

    #	String	Optional. Owner and administrators only. Custom title for this user
    custom_title = ""
    #	Integer	Optional. Restricted and kicked only. Date when restrictions will be lifted for this user; unix time
    until_date = 0
    #	Boolean	Optional. Administrators only. True, if the bot is allowed to edit administrator privileges of that user
    can_be_edited = False
    #	Boolean	Optional. Administrators only. True, if the administrator can post in the channel; channels only
    can_post_messages = False
    #	Boolean	Optional. Administrators only. True, if the administrator can edit messages of other users and can pin messages; channels only
    can_edit_messages = False
    #	Boolean	Optional. Administrators only. True, if the administrator can delete messages of other users
    can_delete_messages = False
    #	Boolean	Optional. Administrators only. True, if the administrator can restrict, ban or unban chat members
    can_restrict_members = False
    #	Boolean	Optional. Administrators only. True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    can_promote_members = False
    #	Boolean	Optional. Administrators and restricted only. True, if the user is allowed to change the chat title, photo and other settings
    can_change_info = False
    #	Boolean	Optional. Administrators and restricted only. True, if the user is allowed to invite new users to the chat
    can_invite_users = False
    #	Boolean	Optional. Administrators and restricted only. True, if the user is allowed to pin messages; groups and supergroups only
    can_pin_messages = False
    #	Boolean	Optional. Restricted only. True, if the user is a member of the chat at the moment of the request
    is_member = False
    #	Boolean	Optional. Restricted only. True, if the user is allowed to send text messages, contacts, locations and venues
    can_send_messages = False
    #	Boolean	Optional. Restricted only. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    can_send_media_messages = False
    #	Boolean	Optional. Restricted only. True, if the user is allowed to send polls
    can_send_polls = False
    #	Boolean	Optional. Restricted only. True, if the user is allowed to send animations, games, stickers and use inline bots
    can_send_other_messages = False
    #	Boolean	Optional. Restricted only. True, if the user is allowed to add web page previews to their messages
    can_add_web_page_previews = False


    def __init__(self, obj):
        self.setUser(obj['user'])
        self.setStatus(obj['status'])
        if 'custom_title' in obj:
            self.setCustomTitle(obj['custom_title'])
        if 'until_date' in obj:
            self.setUntilDate(obj['until_date'])
        if 'can_be_edited' in obj:
            self.setCanBeEdited(obj['can_be_edited'])
        if 'can_post_messages' in obj:
            self.setCanPostMessages(obj['can_post_messages'])
        if 'can_edit_messages' in obj:
            self.setCanEditMessages(obj['can_edit_messages'])
        if 'can_delete_messages' in obj:
            self.setCanDeleteMessages(obj['can_delete_messages'])
        if 'can_restrict_members' in obj:
            self.setCanRestrictMembers(obj['can_restrict_members'])
        if 'can_promote_members' in obj:
            self.setCanPromoteMembers(obj['can_promote_members'])
        if 'can_change_info' in obj:
            self.setCanChangeInfo(obj['can_change_info'])
        if 'can_invite_users' in obj:
            self.setCanInviteUsers(obj['can_invite_users'])
        if 'can_pin_messages' in obj:
            self.setCanPinMessages(obj['can_pin_messages'])
        if 'is_member' in obj:
            self.setIsMember(obj['is_member'])
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


    # запись объекта класса User
    def setUser(self, val):
        self.user = User(val)

    # получение объекта класса User
    def getUser(self):
        return self.user


    # запись
    def setStatus(self, val):
        self.status = val

    # получение
    def getStatus(self):
        return self.status


    # запись
    def setCustomTitle(self, val):
        self.custom_title = val

    # получение
    def getCustomTitle(self):
        return self.custom_title


    # запись
    def setUntilDate(self, val):
        self.until_date = val

    # получение
    def getUntilDate(self):
        return self.until_date


    # запись
    def setCanBeEdited(self, val):
        self.can_be_edited = val

    # получение
    def getCanBeEdited(self):
        return self.can_be_edited


    # запись
    def setCanPostMessages(self, val):
        self.can_post_messages = val

    # получение
    def getCanPostMessages(self):
        return self.can_post_messages


    # запись
    def setCanEditMessages(self, val):
        self.can_edit_messages = val

    # получение
    def getCanEditMessages(self):
        return self.can_edit_messages


    # запись
    def setCanDeleteMessages(self, val):
        self.can_delete_messages = val

    # получение
    def getCanDeleteMessages(self):
        return self.can_delete_messages


    # запись
    def setCanRestrictMembers(self, val):
        self.can_restrict_members = val

    # получение
    def getCanRestrictMembers(self):
        return self.can_restrict_members


    # запись
    def setCanPromoteMembers(self, val):
        self.can_promote_members = val

    # получение
    def getCanPromoteMembers(self):
        return self.can_promote_members


    # запись
    def setCanChangeInfo(self, val):
        self.can_change_info = val

    # получение
    def getCanChangeInfo(self):
        return self.can_change_info


    # запись
    def setCanInviteUsers(self, val):
        self.can_invite_users = val

    # получение
    def getCanInviteUsers(self):
        return self.can_invite_users


    # запись
    def setCanPinMessages(self, val):
        self.can_pin_messages = val

    # получение
    def getCanPinMessages(self):
        return self.can_pin_messages


    # запись
    def setIsMember(self, val):
        self.is_member = val

    # получение
    def getIsMember(self):
        return self.is_member


    # запись
    def setCanSendMessages(self, val):
        self.can_send_messages = val

    # получение
    def getCanSendMessages(self):
        return self.can_send_messages


    # запись
    def setCanSendMediaMessages(self, val):
        self.can_send_media_messages = val

    # получение
    def getCanSendMediaMessages(self):
        return self.can_send_media_messages


    # запись
    def setCanSendPolls(self, val):
        self.can_send_polls = val

    # получение
    def getCanSendPolls(self):
        return self.can_send_polls


    # запись
    def setCanSendOtherMessages(self, val):
        self.can_send_other_messages = val

    # получение
    def getCanSendOtherMessages(self):
        return self.can_send_other_messages


    # запись
    def setCanAddWebPagePreviews(self, val):
        self.can_add_web_page_previews = val

    # получение
    def getCanAddWebPagePreviews(self):
        return self.can_add_web_page_previews



