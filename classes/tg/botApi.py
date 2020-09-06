import requests
import json

from classes.tg.types.update import Update
from classes.tg.types.webhookInfo import WebhookInfo
from classes.tg.types.chat import Chat


class Bot:
    'Class Telegram Bot'

    # variables class Bot
    token = None
    urlApi = "https://api.telegram.org/bot"


    # constuctor
    def __init__(self, token):
        self.token = token


    # получение updates
    def start(self, request):
        return Update(json.loads(request.body))


    # curl
    def call(self, method, data = ""):
        if data == "":
            response = requests.post(self.urlApi + self.token + "/" + method)
        else:
            response = requests.post(self.urlApi + self.token + "/" + method, data = data)

        text = json.loads(response.text)
        if (text['ok']):
            return text['result']
        else:
            return "Ошибка! " + text['error_code'] + " " + text['description']


    # method getUpdates
    def getUpdates(self):
        response = self.call("getUpdates")
        return response


    # method setWebhook
    def setWebhook(self, url):
        response = self.call("setWebhook", "?url=" + str(url))
        return response


    # method deleteWebhook
    def deleteWebhook(self):
        response = self.call("deleteWebhook")
        return response


    # method getWebhookInfo
    def getWebhookInfo(self):
        response = self.call("getWebhookInfo")
        return WebhookInfo(response)


    # method getMe
    def getMe(self):
        response = self.call("getMe")
        return response


    # method sendMessage
    def sendMessage(self, chat_id, text,
            parse_mode = "",
            disable_web_page_preview = None,
            disable_notification = None,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'text':text}
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if disable_web_page_preview is not None:
            data.update({'disable_web_page_preview':disable_web_page_preview})
        if disable_notification is not None:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})
            #data['reply_markup'] = json.dumps(reply_markup)

        response = self.call("sendMessage", data)
        return response


    # method forwardMessage
    def forwardMessage(self, chat_id, from_chat_id, message_id,
            disable_notification = False):

        data = {
            'chat_id':chat_id,
            'from_chat_id':from_chat_id,
            'message_id':message_id
        }
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})

        response = self.call("forwardMessage", data)
        return response


    # method sendPhoto
    def sendPhoto(self, chat_id, photo,
            caption = "",
            parse_mode = "",
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'photo':photo}
        if caption != "":
            data.update({'caption':caption})
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendPhoto", data)
        return response


    # method sendAudio
    def sendAudio(self, chat_id, audio,
            caption = "",
            parse_mode = "",
            duration = 0,
            performer = "",
            title = "",
            thumb = "",
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'audio':audio}
        if caption != "":
            data.update({'caption':caption})
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if duration != 0:
            data.update({'duration':duration})
        if performer != "":
            data.update({'performer':performer})
        if title != "":
            data.update({'title':title})
        if thumb != "":
            data.update({'thumb':thumb})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendAudio", data)
        return response


    # method sendDocument  работает лишь с file_id
    def sendDocument(self, chat_id, document,
            thumb = "",
            caption = "",
            parse_mode = "",
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'document':document}
        if thumb != "":
            data.update({'thumb':thumb})
        if caption != "":
            data.update({'caption':caption})
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendDocument", data)
        return response


    # method sendVideo  работает лишь с file_id
    def sendVideo(self, chat_id, video,
            duration = 0,
            width = 0,
            height = 0,
            thumb = "",
            caption = "",
            parse_mode = "",
            supports_streaming = False,
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'video':video}
        if duration != 0:
            data.update({'duration':duration})
        if width != 0:
            data.update({'width':width})
        if height != 0:
            data.update({'height':height})
        if thumb != "":
            data.update({'thumb':thumb})
        if caption != "":
            data.update({'caption':caption})
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if supports_streaming != "":
            data.update({'supports_streaming':supports_streaming})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendVideo", data)
        return response


    # method sendAnimation  работает лишь с file_id
    #(почему-то стикеры отправляются, а что тогда анимация?)
    def sendAnimation(self, chat_id, animation,
            duration = 0,
            width = 0,
            height = 0,
            thumb = "",
            caption = "",
            parse_mode = "",
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'animation':animation}
        if duration != 0:
            data.update({'duration':duration})
        if width != 0:
            data.update({'width':width})
        if height != 0:
            data.update({'height':height})
        if thumb != "":
            data.update({'thumb':thumb})
        if caption != "":
            data.update({'caption':caption})
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendAnimation", data)
        return response


# method sendVoice
    def sendVoice(self, chat_id, voice,
            caption = "",
            parse_mode = "",
            duration = 0,
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'voice':voice}
        if caption != "":
            data.update({'caption':caption})
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if duration != 0:
            data.update({'duration':duration})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendVoice", data)
        return response


    # method sendVideoNote  работает лишь с file_id
    def sendVideoNote(self, chat_id, video_note,
            duration = 0,
            length = 0,
            thumb = "",
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'video_note':video_note}
        if duration != 0:
            data.update({'duration':duration})
        if length != 0:
            data.update({'length':length})
        if thumb != "":
            data.update({'thumb':thumb})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendVideoNote", data)
        return response


    # method sendMediaGroup
    def sendMediaGroup(self, chat_id, media,
            disable_notification = False,
            reply_to_message_id = 0):

        data = {'chat_id':chat_id, 'media':media}
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})

        response = self.call("sendMediaGroup", data)
        return response





    # method sendLocation
    def sendLocation(self, chat_id, latitude, longitude,
            live_period = 0,
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'latitude':latitude, 'longitude':longitude}
        if live_period != 0:
            data.update({'live_period':live_period})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendLocation", data)
        return response


    # method editMessageLiveLocation
    def editMessageLiveLocation(self,
            chat_id = None,
            message_id = 0,
            latitude = 0,
            longitude = 0,
            inline_message_id = 0,
            reply_markup = None):

        data = {'latitude':latitude, 'longitude':longitude}
        if chat_id is not None:
            data.update({'chat_id':chat_id})
            if message_id != 0:
                data.update({'message_id':message_id})
            else:
                return False
        elif inline_message_id != 0:
            data.update({'inline_message_id':inline_message_id})
        else:
            return False
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("editMessageLiveLocation", data)
        return response


    # method stopMessageLiveLocation
    def stopMessageLiveLocation(self,
            chat_id = None,
            message_id = 0,
            inline_message_id = 0,
            reply_markup = None):

        data = {}
        if chat_id is not None:
            data.update({'chat_id':chat_id})
            if message_id != 0:
                data.update({'message_id':message_id})
            else:
                return False
        elif inline_message_id != 0:
            data.update({'inline_message_id':inline_message_id})
        else:
            return False
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("stopMessageLiveLocation", data)
        return response


    # method sendVenue
    def sendVenue(self, chat_id, latitude, longitude, title, address,
            foursquare_id = "",
            foursquare_type = "",
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {
            'chat_id':chat_id,
            'latitude':latitude,
            'longitude':longitude,
            'title':title,
            'address':address
        }
        if foursquare_id != "":
            data.update({'foursquare_id':foursquare_id})
        if foursquare_type != "":
            data.update({'foursquare_type':foursquare_type})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendVenue", data)
        return response


    # method sendContact
    def sendContact(self, chat_id, phone_number, first_name,
            last_name = "",
            vcard = "",
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'phone_number':phone_number, 'first_name':first_name}
        if last_name != "":
            data.update({'last_name':last_name})
        if vcard != "":
            data.update({'vcard':vcard})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendContact", data)
        return response


    # method sendPoll
    def sendPoll(self, chat_id, question, options,
            is_anonymous = False,
            type = "",
            allows_multiple_answers = False,
            correct_option_id = 0,
            explanation = "",
            explanation_parse_mode = "",
            open_period = 0,
            close_date = 0,
            is_closed = False,
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'question':question, 'options':options}
        if is_anonymous != False:
            data.update({'is_anonymous':is_anonymous})
        if type != "":
            data.update({'type':type})
        if allows_multiple_answers != False:
            data.update({'allows_multiple_answers':allows_multiple_answers})
        if correct_option_id != 0:
            data.update({'correct_option_id':correct_option_id})
        if explanation != "":
            data.update({'explanation':explanation})
        if explanation_parse_mode != "":
            data.update({'explanation_parse_mode':explanation_parse_mode})
        if open_period != 0:
            data.update({'open_period':open_period})
        if close_date != 0:
            data.update({'close_date':close_date})
        if is_closed != False:
            data.update({'is_closed':is_closed})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendPoll", data)
        return response


    # method sendDice
    def sendDice(self, chat_id,
            emoji = "",
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id}
        if emoji != "":
            data.update({'emoji':emoji})
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendDice", data)
        return response


    # method sendChatAction
    def sendChatAction(self, chat_id, action):

        data = {'chat_id':chat_id, 'action':action}

        response = self.call("sendChatAction", data)
        return response


    # method getUserProfilePhotos
    def getUserProfilePhotos(self, user_id,
            offset = 0,
            limit = 0):

        data = {'user_id':user_id}
        if offset != 0:
            data.update({'offset':offset})
        if limit != 0:
            data.update({'limit':limit})

        response = self.call("getUserProfilePhotos", data)
        return response


    # method getFile
    def getFile(self, file_id):

        data = {'file_id':file_id}

        response = self.call("getFile", data)
        return response


    # method kickChatMember
    def kickChatMember(self, chat_id, user_id,
            until_date = 0):

        data = {'chat_id':chat_id, 'user_id':user_id}
        if until_date != 0:
            data.update({'until_date':until_date})

        response = self.call("kickChatMember", data)
        return response


    # method unbanChatMember
    def unbanChatMember(self, chat_id, user_id):

        data = {'chat_id':chat_id, 'user_id':user_id}

        response = self.call("unbanChatMember", data)
        return response


    # method restrictChatMember
    # permissions - class ChatPermissions, A JSON-serialized object for new user permissions
    def restrictChatMember(self, chat_id, user_id, permissions,
            until_date = 0):

        data = {'chat_id':chat_id, 'user_id':user_id, 'permissions':json.dumps(permissions)}
        if until_date != 0:
            data.update({'until_date':until_date})

        response = self.call("restrictChatMember", data)
        return response


    # method promoteChatMember
    def promoteChatMember(self, chat_id, user_id,
            can_change_info = False,
            can_post_messages = False,
            can_edit_messages = False,
            can_delete_messages = False,
            can_invite_users = False,
            can_restrict_members = False,
            can_pin_messages = False,
            can_promote_members = False):

        data = {'chat_id':chat_id, 'user_id':user_id}
        if can_change_info != False:
            data.update({'can_change_info':can_change_info})
        if can_post_messages != False:
            data.update({'can_post_messages':can_post_messages})
        if can_edit_messages != False:
            data.update({'can_edit_messages':can_edit_messages})
        if can_delete_messages != False:
            data.update({'can_delete_messages':can_delete_messages})
        if can_invite_users != False:
            data.update({'can_invite_users':can_invite_users})
        if can_restrict_members != False:
            data.update({'can_restrict_members':can_restrict_members})
        if can_pin_messages != False:
            data.update({'can_pin_messages':can_pin_messages})
        if can_promote_members != False:
            data.update({'can_promote_members':can_promote_members})

        response = self.call("promoteChatMember", data)
        return response


    # method setChatAdministratorCustomTitle
    def setChatAdministratorCustomTitle(self, chat_id, user_id, custom_title):

        data = {'chat_id':chat_id, 'user_id':user_id, 'custom_title':custom_title}

        response = self.call("setChatAdministratorCustomTitle", data)
        return response


    # method setChatPermissions
    def setChatPermissions(self, chat_id, permissions):

        data = {'chat_id':chat_id, 'permissions':permissions}

        response = self.call("setChatPermissions", data)
        return response


    # method exportChatInviteLink
    def exportChatInviteLink(self, chat_id):

        data = {'chat_id':chat_id}

        response = self.call("exportChatInviteLink", data)
        return response


    # method setChatPhoto
    def setChatPhoto(self, chat_id, photo):

        data = {'chat_id':chat_id, 'photo':photo}

        response = self.call("setChatPhoto", data)
        return response


    # method deleteChatPhoto
    def deleteChatPhoto(self, chat_id):

        data = {'chat_id':chat_id}

        response = self.call("deleteChatPhoto", data)
        return response


    # method setChatTitle
    def setChatTitle(self, chat_id, title):

        data = {'chat_id':chat_id, 'title':title}

        response = self.call("setChatTitle", data)
        return response


    # method setChatDescription
    def setChatDescription(self, chat_id,
            description = ""):

        data = {'chat_id':chat_id}
        if description != "":
            data.update({'description':description})

        response = self.call("setChatDescription", data)
        return response


    # method pinChatMessage
    def pinChatMessage(self, chat_id, message_id,
            disable_notification = False):

        data = {'chat_id':chat_id, 'message_id':message_id}
        if disable_notification != False:
            data.update({'disable_notification':disable_notification})

        response = self.call("pinChatMessage", data)
        return response


    # method unpinChatMessage
    def unpinChatMessage(self, chat_id):

        data = {'chat_id':chat_id}

        response = self.call("unpinChatMessage", data)
        return response


    # method leaveChat
    def leaveChat(self, chat_id):

        data = {'chat_id':chat_id}

        response = self.call("leaveChat", data)
        return response


    # method getChat
    def getChat(self, chat_id):

        data = {'chat_id':chat_id}

        response = self.call("getChat", data)
        return Chat(response)


    # method getChatAdministrators
    def getChatAdministrators(self, chat_id):

        data = {'chat_id':chat_id}

        response = self.call("getChatAdministrators", data)
        return response


    # method getChatMembersCount
    def getChatMembersCount(self, chat_id):

        data = {'chat_id':chat_id}

        response = self.call("getChatMembersCount", data)
        return response


    # method getChatMember
    def getChatMember(self, chat_id, user_id):

        data = {'chat_id':chat_id, 'user_id':user_id}

        response = self.call("getChatMember", data)
        return response


    # method setChatStickerSet
    def setChatStickerSet(self, chat_id, sticker_set_name):

        data = {'chat_id':chat_id, 'sticker_set_name':sticker_set_name}

        response = self.call("setChatStickerSet", data)
        return response


    # method deleteChatStickerSet
    def deleteChatStickerSet(self, chat_id):

        data = {'chat_id':chat_id}

        response = self.call("deleteChatStickerSet", data)
        return response


    # method answerCallbackQuery
    def answerCallbackQuery(self, callback_query_id,
            text = "",
            show_alert = False,
            url = "",
            cache_time = 0):

        data = {'callback_query_id':callback_query_id}
        if text != "":
            data.update({'text':text})
        if show_alert != False:
            data.update({'show_alert':show_alert})
        if url != "":
            data.update({'url':url})
        if cache_time != 0:
            data.update({'cache_time':cache_time})

        response = self.call("answerCallbackQuery", data)
        return response


    # method setMyCommands
    # commands Array of object class BotCommand - A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.
    def setMyCommands(self, commands):

        data = {'commands':commands}

        response = self.call("setMyCommands", data)
        return response


    # method getMyCommands
    def getMyCommands(self):
        return self.call("getMyCommands")


    # method editMessageText
    def editMessageText(self,
            chat_id = None,
            message_id = 0,
            text = "",
            inline_message_id = "",
            parse_mode = "",
            disable_web_page_preview = False,
            reply_markup = None):

        data = {'text':text}
        if chat_id is not None:
            data.update({'chat_id':chat_id})
            if message_id != 0:
                data.update({'message_id':message_id})
            else:
                return False
        elif inline_message_id != "":
            data.update({'inline_message_id':inline_message_id})
        else:
            return False
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if disable_web_page_preview == True:
            data.update({'disable_web_page_preview':disable_web_page_preview})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("editMessageText", data)
        return response


    # method editMessageCaption
    def editMessageCaption(self,
            chat_id = None,
            message_id = 0,
            inline_message_id = "",
            caption = "",
            parse_mode = "",
            reply_markup = None):

        data = {}
        if chat_id is not None:
            data.update({'chat_id':chat_id})
            if message_id != 0:
                data.update({'message_id':message_id})
            else:
                return False
        elif inline_message_id != "":
            data.update({'inline_message_id':inline_message_id})
        else:
            return False
        if caption != "":
            data.update({'caption':caption})
        if parse_mode != "":
            data.update({'parse_mode':parse_mode})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("editMessageCaption", data)
        return response


    # method editMessageMedia
    def editMessageMedia(self,
            chat_id = None,
            message_id = 0,
            media = "",
            inline_message_id = "",
            reply_markup = None):

        data = {'media':media}
        if chat_id is not None:
            data.update({'chat_id':chat_id})
            if message_id != 0:
                data.update({'message_id':message_id})
            else:
                return False
        elif inline_message_id != "":
            data.update({'inline_message_id':inline_message_id})
        else:
            return False
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("editMessageMedia", data)
        return response


    # method editMessageReplyMarkup
    def editMessageReplyMarkup(self,
            chat_id = None,
            message_id = 0,
            inline_message_id = "",
            reply_markup = None):

        data = {}
        if chat_id is not None:
            data.update({'chat_id':chat_id})
            if message_id != 0:
                data.update({'message_id':message_id})
            else:
                return False
        elif inline_message_id != "":
            data.update({'inline_message_id':inline_message_id})
        else:
            return False
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("editMessageReplyMarkup", data)
        return response


    # method stopPoll
    def stopPoll(self, chat_id, message_id,
            reply_markup = None):

        data = {'chat_id':chat_id, 'message_id':message_id}
        if reply_markup is not None:
            data.update({'reply_markup':reply_markup})

        response = self.call("stopPoll", data)
        return response


    # method deleteMessage
    def deleteMessage(self, chat_id, message_id):

        data = {'chat_id':chat_id, 'message_id':message_id}

        response = self.call("deleteMessage", data)
        return response


    '''
    -------------------
    |     STICKER     |
    -------------------
    '''


    # method sendSticker
    def sendSticker(self, chat_id, sticker,
            disable_notification = False,
            reply_to_message_id = 0,
            reply_markup = None):

        data = {'chat_id':chat_id, 'sticker':sticker}
        if disable_notification == True:
            data.update({'disable_notification':disable_notification})
        if reply_to_message_id != 0:
            data.update({'reply_to_message_id':reply_to_message_id})
        if reply_markup is not None:
            data.update({'reply_markup':json.dumps(reply_markup)})

        response = self.call("sendSticker", data)
        return response


    # method getStickerSet
    def getStickerSet(self, name):

        data = {'name':name}

        response = self.call("getStickerSet", data)
        return response


    # method uploadStickerFile
    def uploadStickerFile(self, user_id, png_sticker):

        data = {'user_id':user_id, 'png_sticker':png_sticker}

        response = self.call("uploadStickerFile", data)
        return response


    # method createNewStickerSet
    def createNewStickerSet(self, user_id, name, title, emojis,
            png_sticker = None,
            tgs_sticker = None,
            contains_masks = False,
            mask_position = None):

        data = {'user_id':user_id, 'name':name, 'title':title, 'emojis':emojis}
        if png_sticker is not None:
            data.update({'png_sticker':png_sticker})
        if tgs_sticker is not None:
            data.update({'tgs_sticker':tgs_sticker})
        if contains_masks != False:
            data.update({'contains_masks':contains_masks})
        if mask_position is not None:
            data.update({'mask_position':json.dumps(mask_position)})

        response = self.call("createNewStickerSet", data)
        return response


    # method addStickerToSet
    def addStickerToSet(self, user_id, name, emojis,
            png_sticker = None,
            tgs_sticker = None,
            mask_position = None):

        data = {'user_id':user_id, 'name':name, 'emojis':emojis}
        if png_sticker is not None:
            data.update({'png_sticker':png_sticker})
        if tgs_sticker is not None:
            data.update({'tgs_sticker':tgs_sticker})
        if mask_position is not None:
            data.update({'mask_position':json.dumps(mask_position)})

        response = self.call("addStickerToSet", data)
        return response


    # method setStickerPositionInSet
    def setStickerPositionInSet(self, sticker, position):

        data = {'sticker':sticker, 'position':position}

        response = self.call("setStickerPositionInSet", data)
        return response


    # method deleteStickerFromSet
    def deleteStickerFromSet(self, sticker):

        data = {'sticker':sticker}

        response = self.call("deleteStickerFromSet", data)
        return response


    # method setStickerSetThumb
    def setStickerSetThumb(self, name, user_id,
            thumb = None):

        data = {'name':name, 'user_id':user_id}

        if thumb is not None:
            data.update({'thumb':thumb})

        response = self.call("setStickerSetThumb", data)
        return response



    '''
    -------------------
    |   INLINE MODE   |
    -------------------
    '''






