from classes.tg.types.user import User
from classes.tg.types.chat import Chat
from classes.tg.types.messageEntity import MessageEntity
from classes.tg.types.animation import Animation
from classes.tg.types.audio import Audio
from classes.tg.types.document import Document
from classes.tg.types.photoSize import PhotoSize
from classes.tg.types.sticker import Sticker
from classes.tg.types.video import Video
from classes.tg.types.videoNote import VideoNote
from classes.tg.types.voice import Voice
from classes.tg.types.contact import Contact
from classes.tg.types.dice import Dice
from classes.tg.types.game import Game
from classes.tg.types.poll import Poll
from classes.tg.types.venue import Venue
from classes.tg.types.location import Location
from classes.tg.types.invoice import Invoice
from classes.tg.types.successfulPayment import SuccessfulPayment
from classes.tg.types.passportData import PassportData
from classes.tg.types.inlineKeyboardMarkup import InlineKeyboardMarkup

import json


class Message:
    'телеграм объект типа Message'

    # Integer	Unique message identifier inside this chat
    message_id = 0

    # объект класса User (Optional). Sender, empty for messages sent to channels
    message_from = None

    # Integer  Date the message was sent in Unix time
    date = 0
    # объект класса Chat	Conversation the message belongs to
    chat = None

    # объект класса User (Optional). For forwarded messages, sender of the original message
    forward_from = None
    # объект класса Chat	(Optional). For messages forwarded from channels, information about the original channel
    forward_from_chat = None
    # Integer	(Optional). For messages forwarded from channels, identifier of the original message in the channel
    forward_from_message_id = 0
    # String	(Optional). For messages forwarded from channels, signature of the post author if present
    forward_signature = ""
    # String	(Optional). Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    forward_sender_name = ""
    # Integer	(Optional). For forwarded messages, date the original message was sent in Unix time
    forward_date = 0
    # объект класса Message	(Optional). For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    reply_to_message = None
    # объект класса User	(Optional). Bot through which the message was sent
    via_bot = None
    # Integer	(Optional). Date the message was last edited in Unix time
    edit_date = 0
    # String	(Optional). The unique identifier of a media message group this message belongs to
    media_group_id = ""
    # String (Optional) Signature of the post author for messages in channels
    author_signature = ""
    # String (Optional) For text messages, the actual UTF-8 text of the message, 0-4096 characters
    text = ""
    # Array объектов класса MessageEntity	(Optional). For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    entities = []

    # объект класса Animation	(Optional). Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
    animation = None

    # объект класса Audio	(Optional). Message is an audio file, information about the file
    audio = None
    # объект класса Document	(Optional). Message is a general file, information about the file
    document = None
    # Array объектов класса PhotoSize	(Optional). Message is a photo, available sizes of the photo
    photo = []
    # объект класса Sticker	(Optional). Message is a sticker, information about the sticker
    sticker = None
    # объект класса Video	(Optional). Message is a video, information about the video
    video = None
    # объект класса VideoNote	(Optional). Message is a video note, information about the video message
    video_note = None
    # объект класса Voice	(Optional). Message is a voice message, information about the file
    voice = None
    # String	(Optional). Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    caption = ""

    # Array объектов класса MessageEntity	(Optional). For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    caption_entities = []
    # объект класса Contact	(Optional). Message is a shared contact, information about the contact
    contact = None
    # объект класса Dice	(Optional). Message is a dice with random value from 1 to 6
    dice = None
    # объект класса Game	(Optional). Message is a game, information about the game. More about games »
    game = None
    # объект класса Poll	(Optional). Message is a native poll, information about the poll
    poll = None
    # объект класса Venue	(Optional). Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
    venue = None
    # объект класса Location	(Optional). Message is a shared location, information about the location
    location = None

    # Array объектов класса User	(Optional). New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    new_chat_members = []
    # объект класса User	(Optional). A member was removed from the group, information about them (this member may be the bot itself)
    left_chat_member = None
    # String	(Optional). A chat title was changed to this value
    new_chat_title = ""
    # Array объектов класса PhotoSize	(Optional). A chat photo was change to this value
    new_chat_photo = []
    # True	(Optional). Service message: the chat photo was deleted
    delete_chat_photo = None
    # True	(Optional). Service message: the group has been created
    group_chat_created = None
    # True	(Optional). Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    supergroup_chat_created = None
    # True	(Optional). Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    channel_chat_created = None
    # Integer	(Optional). The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    migrate_to_chat_id = 0
    # Integer	(Optional). The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    migrate_from_chat_id = 0
    # объект класса Message	(Optional). Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
    pinned_message = None
    # объект класса Invoice	(Optional). Message is an invoice for a payment, information about the invoice. More about payments »
    invoice = None
    # объект класса SuccessfulPayment	(Optional). Message is a service message about a successful payment, information about the payment. More about payments »
    successful_payment = None
    # String	(Optional). The domain name of the website on which the user has logged in. More about Telegram Login »
    connected_website = ""
    # объект класса PassportData	(Optional). Telegram Passport data
    passport_data = None
    # объект класса InlineKeyboardMarkup	(Optional). Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    reply_markup = None


    # конструктор
    def __init__(self, obj):
        self.setMessageId(obj['message_id'])
        if 'from' in obj:
            self.setFrom(obj['from'])
        self.setDate(obj['date'])
        self.setChat(obj['chat'])
        if 'forward_from' in obj:
            self.setForwardFrom(obj['forward_from'])
        if 'forward_from_chat' in obj:
            self.setForwardFromChat(obj['forward_from_chat'])
        if 'forward_from_message_id' in obj:
            self.setForwardFromMessageId(obj['forward_from_message_id'])
        if 'forward_signature' in obj:
            self.setForwardSignature(obj['forward_signature'])
        if 'forward_sender_name' in obj:
            self.setForwardSenderName(obj['forward_sender_name'])
        if 'forward_date' in obj:
            self.setForwardDate(obj['forward_date'])
        if 'reply_to_message' in obj:
            self.setReplyToMessage(obj['reply_to_message'])
        if 'via_bot' in obj:
            self.setViaBot(obj['via_bot'])
        if 'edit_date' in obj:
            self.setEditDate(obj['edit_date'])
        if 'media_group_id' in obj:
            self.setMediaGroupId(obj['media_group_id'])
        if 'author_signature' in obj:
            self.setAuthorSignature(obj['author_signature'])
        if 'text' in obj:
            self.setText(obj['text'])
        if 'entities' in obj:
            self.setEntities(obj['entities'])
        if 'animation' in obj:
            self.setAnimation(obj['animation'])
        if 'audio' in obj:
            self.setAudio(obj['audio'])
        if 'document' in obj:
            self.setDocument(obj['document'])
        if 'photo' in obj:
            self.setPhoto(obj['photo'])
        if 'sticker' in obj:
            self.setSticker(obj['sticker'])
        if 'video' in obj:
            self.setVideo(obj['video'])
        if 'video_note' in obj:
            self.setVideoNote(obj['video_note'])
        if 'voice' in obj:
            self.setVoice(obj['voice'])
        if 'caption' in obj:
            self.setCaption(obj['caption'])
        if 'caption_entities' in obj:
            self.setCaptionEntities(obj['caption_entities'])
        '''
        if 'contact' in obj:
            self.setContact(obj['contact'])
        '''
        if 'dice' in obj:
            self.setDice(obj['dice'])
        if 'game' in obj:
            self.setGame(obj['game'])
        if 'poll' in obj:
            self.setPoll(obj['poll'])
        if 'venue' in obj:
            self.setVenue(obj['venue'])
        if 'location' in obj:
            self.setLocation(obj['location'])
        if 'new_chat_members' in obj:
            self.setNewChatMembers(obj['new_chat_members'])
        if 'left_chat_member' in obj:
            self.setLeftChatMember(obj['left_chat_member'])
        if 'new_chat_title' in obj:
            self.setNewChatTitle(obj['new_chat_title'])
        if 'new_chat_photo' in obj:
            self.setNewChatPhoto(obj['new_chat_photo'])
        if 'delete_chat_photo' in obj:
            self.setDeleteChatPhoto(obj['delete_chat_photo'])
        if 'group_chat_created' in obj:
            self.setGroupChatCreated(obj['group_chat_created'])
        if 'supergroup_chat_created' in obj:
            self.setSupergroupChatCreated(obj['supergroup_chat_created'])
        if 'channel_chat_created' in obj:
            self.setChannelChatCreated(obj['channel_chat_created'])
        if 'migrate_to_chat_id' in obj:
            self.setMigrateToChatId(obj['migrate_to_chat_id'])
        if 'migrate_from_chat_id' in obj:
            self.setMigrateFromChatId(obj['migrate_from_chat_id'])
        if 'pinned_message' in obj:
            self.setPinnedMessage(obj['pinned_message'])
        if 'invoice' in obj:
            self.setInvoice(obj['invoice'])
        if 'successful_payment' in obj:
            self.setSuccessfulPayment(obj['successful_payment'])
        if 'connected_website' in obj:
            self.setConnectedWebsite(obj['connected_website'])
        if 'passport_data' in obj:
            self.setPassportData(obj['passport_data'])
        if 'reply_markup' in obj:
            self.setReplyMarkup(obj['reply_markup'])



    def get(self):
        response = {
            'message_id':self.message_id,
            'date':self.date,
            'chat':self.chat.get()
        }

        if self.message_from is not None:
            response.update({'from':self.message_from.get()})
        if self.forward_from is not None:
            response.update({'forward_from':self.forward_from.get()})
        if self.forward_from_chat is not None:
            response.update({'forward_from_chat':self.forward_from_chat.get()})
        if self.forward_from_message_id != 0:
            response.update({'forward_from_message_id':self.forward_from_message_id})
        if self.forward_signature != "":
            response.update({'forward_signature':self.forward_signature})
        if self.forward_sender_name != "":
            response.update({'forward_sender_name':self.forward_sender_name})
        if self.forward_date != 0:
            response.update({'forward_date':self.forward_date})
        if self.reply_to_message is not None:
            response.update({'reply_to_message':self.reply_to_message.get()})
        if self.via_bot is not None:
            response.update({'via_bot':self.via_bot.get()})
        if self.edit_date != 0:
            response.update({'edit_date':self.edit_date})
        if self.media_group_id != "":
            response.update({'media_group_id':self.media_group_id})
        if self.author_signature != "":
            response.update({'author_signature':self.author_signature})
        if self.text != "":
            response.update({'text':self.text})
        if self.entities != []:
            entit = []
            i = 0
            while i < len(self.entities):
                entit.append(self.entities[i].get())
                i += 1
            response.update({'entities':entit})

        if self.animation is not None:
            response.update({'animation':self.animation.get()})

        if self.audio is not None:
            response.update({'audio':self.audio.get()})
        if self.document is not None:
            response.update({'document':self.document.get()})
        if self.photo != []:
            phot = []
            i = 0
            while i < len(self.photo):
                phot.append(self.photo[i].get())
                i += 1
            response.update({'photo':phot})
        if self.sticker is not None:
            response.update({'sticker':self.sticker.get()})
        if self.video is not None:
            response.update({'video':self.video.get()})
        if self.video_note is not None:
            response.update({'video_note':self.video_note.get()})
        if self.voice is not None:
            response.update({'voice':self.voice.get()})
        if self.caption != "":
            response.update({'caption':self.caption})

        if self.caption_entities != []:
            caption_ent = []
            i = 0
            while i < len(self.caption_entities):
                caption_ent.append(self.caption_entities[i].get())
                i += 1
            response.update({'caption_entities':caption_ent})
        '''
        if self.contact is not None:
            response.update({'contact':self.contact.get()})
        '''
        if self.dice is not None:
            response.update({'dice':self.dice.get()})
        '''
        if self.game is not None:
            response.update({'game':self.game.get()})
        if self.poll is not None:
            response.update({'poll':self.poll.get()})
        '''

        '''
        if self.venue is not None:
            response.update({'venue':self.venue.get()})
        if self.location is not None:
            response.update({'location':self.location.get()})
        '''

        if self.reply_markup is not None:
            response.update({'reply_markup':self.reply_markup.get()})

        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    # запись id сообщения
    def setMessageId(self, msgId):
        self.message_id = msgId

    # получение id сообщения
    def getMessageId(self):
        return self.message_id


    # запись объекта класса User
    def setFrom(self, msgFrom):
        self.message_from = User(msgFrom)

    # получение объекта класса User
    def getFrom(self):
        return self.message_from


    # запись даты
    def setDate(self, dt):
        self.date = dt

    # получение даты
    def getDate(self):
        return self.date


    # запись объекта класса Chat
    def setChat(self, cht):
        self.chat = Chat(cht)

    # получение объекта класса Chat
    def getChat(self):
        return self.chat


    # запись объекта класса User
    def setForwardFrom(self, val):
        self.forward_from = User(val)

    # получение объекта класса User
    def getForwardFrom(self):
        return self.forward_from


    # запись объекта класса Chat
    def setForwardFromChat(self, val):
        self.forward_from_chat = Chat(val)

    # получение объекта класса Chat
    def getForwardFromChat(self):
        return self.forward_from_chat


    # запись id пересланного сообщения
    def setForwardFromMessageId(self, val):
        self.forward_from_message_id = val

    # получение id пересланного сообщения
    def getForwardFromMessageId(self):
        return self.forward_from_message_id


    # запись пересланой подписи
    def setForwardSignature(self, val):
        self.forward_signature = val

    # получение пересланой подписи
    def getForwardSignature(self):
        return self.forward_signature


    # запись имени отправителя пересланного сообщения
    def setForwardSenderName(self, val):
        self.forward_sender_name = val

    # получение имени отправителя пересланного сообщения
    def getForwardSenderName(self):
        return self.forward_sender_name


    # запись даты пересланного сообщения
    def setForwardDate(self, val):
        self.forward_date = val

    # получение даты пересланного сообщения
    def getForwardDate(self):
        return self.forward_date


    # запись объекта класса Message
    def setReplyToMessage(self, val):
        self.reply_to_message = Message(val)

    # получение объекта класса Message
    def  getReplyToMessage(self):
        return self.reply_to_message


    # запись объекта класса User
    def setViaBot(self, val):
        self.via_bot = User(val)

    # получение объекта класса User
    def getViaBot(self):
        return self.via_bot


    # запись изменённой дата
    def setEditDate(self, val):
        self.edit_date = val

    # получение изменённой дата
    def getEditDate(self):
        return self.edit_date


    # запись id
    def setMediaGroupId(self, val):
        self.media_group_id =val

    # получение id
    def getMediaGroupId(self):
        return self.media_group_id


    # запись подписи автора
    def setAuthorSignature(self, val):
        self.author_signature = val

    # получение подписи автора
    def getAuthorSignature(self):
        return self.author_signature


    # запись текста сообщения
    def setText(self, txt):
        self.text = txt

    # получение текста сообщения
    def getText(self):
        return self.text


    # запись массива объектов класса MessageEntity
    def setEntities(self, val):
        self.entities = []
        i = 0
        while i < len(val):
            self.entities.append(MessageEntity(val[i]))
            i += 1

    # получение массива объектов класса MessageEntity
    def getEntities(self):
        return self.entities


    # запись объекта класса Animation
    def setAnimation(self, val):
        self.animation = Animation(val)

    # получение объекта класса Animation
    def getAnimation(self):
        return self.animation


    # запись объекта класса Audio
    def setAudio(self, val):
        self.audio = Audio(val)

    # получение объекта класса Audio
    def getAudio(self):
        return self.audio


    # запись объекта класса	Document
    def setDocument(self, val):
        self.document = Document(val)

    # получение объекта класса Document
    def getDocument(self):
        return self.document


    # запись массива объектов класса PhotoSize
    def setPhoto(self, val):
        self.photo = []
        i = 0
        while i < len(val):
            self.photo.append(PhotoSize(val[i]))
            i += 1

    # получение массива объектов класса PhotoSize
    def getPhoto(self):
        return self.photo


    # запись объекта класса Sticker
    def setSticker(self, val):
        self.sticker = Sticker(val)

    # получение объекта класса Sticker
    def getSticker(self):
        return self.sticker


    # запись объекта класса Video
    def setVideo(self, val):
        self.video = Video(val)

    # получение объекта класса Video
    def getVideo(self):
        return self.video


    # запись объекта класса VideoNote
    def setVideoNote(self, val):
        self.video_note = VideoNote(val)

    # получение объекта класса VideoNote
    def getVideoNote(self):
        return self.video_note


    # запись объекта класса Voice
    def setVoice(self, val):
        self.voice = Voice(val)

    # получение объекта класса Voice
    def getVoice(self):
        return self.voice


    # запись
    def setCaption(self, val):
        self.caption =val

    # получение
    def getCaption(self):
        return self.caption


    # запись массива объектов класса MessageEntity
    def setCaptionEntities(self, val):
        self.caption_entities = []
        i = 0
        while i < len(val):
            self.caption_entities.append(MessageEntity(val[i]))
            i += 1

    # получение массива объектов класса MessageEntity
    def getCaptionEntities(self):
        return self.caption_entities

    '''
    # запись объекта класса Contact
    def setContact(self, val):
        self.contact = Contact(val)

    # получение объекта класса Contact
    def getContact(self):
        return self.contact
    '''

        # запись объекта класса Dice
    def setDice(self, val):
        self.dice = Dice(val)

    # получение объекта класса Dice
    def getDice(self):
        return self.dice


    # запись объекта класса Game
    def setGame(self, val):
        self.game = Game(val)

    # получение объекта класса Game
    def getGame(self):
        return self.game


    # запись объекта класса Poll
    def setPoll(self, val):
        self.poll = Poll(val)

    # получение объекта класса Poll
    def getPoll(self):
        return self.poll


    # запись объекта класса Venue
    def setVenue(self, val):
        self.venue = Venue(val)

    # получение объекта класса Venue
    def getVenue(self):
        return self.venue


    # запись объекта класса Location
    def setLocation(self, val):
        self.location = Location(val)

    # получение объекта класса Location
    def getForwardSenderName(self):
        return self.location


    # запись массива объектов класса User
    def setNewChatMembers(self, val):
        self.new_chat_members = []
        i = 0
        while i < len(val):
            self.new_chat_members.append(User(val[i]))
            i += 1

    # получение массива объектов класса User
    def getNewChatMembers(self):
        return self.new_chat_members


    # запись объекта класса User
    def setLeftChatMember(self, val):
        self.left_chat_member = User(val)

    # получение объекта класса User
    def  getLeftChatMember(self):
        return self.left_chat_member


    # запись
    def setNewChatTitle(self, val):
        self.new_chat_title = val

    # получение
    def getNewChatTitle(self):
        return self.new_chat_title


    # запись массива объектов класса PhotoSize
    def setNewChatPhoto(self, val):
        self.new_chat_photo = []
        i = 0
        while i < len(val):
            self.new_chat_photo.append(PhotoSize(val[i]))
            i += 1

    # получение массива объектов класса PhotoSize
    def getNewChatPhoto(self):
        return self.new_chat_photo


    # запись
    def setDeleteChatPhoto(self, val):
        self.delete_chat_photo =val

    # получение
    def getDeleteChatPhoto(self):
        return self.delete_chat_photo


    # запись
    def setGroupChatCreated(self, val):
        self.group_chat_created = val

    # получение
    def getGroupChatCreated(self):
        return self.group_chat_created


    # запись
    def setSupergroupChatCreated(self, val):
        self.supergroup_chat_created = val

    # получение
    def getSupergroupChatCreated(self):
        return self.supergroup_chat_created


    # запись
    def setChannelChatCreated(self, val):
        self.channel_chat_created = val

    # получение
    def getChannelChatCreated(self):
        return self.channel_chat_created


    # запись
    def setMigrateToChatId(self, val):
        self.migrate_to_chat_id = val

    # получение
    def getMigrateToChatId(self):
        return self.migrate_to_chat_id


    # запись
    def setMigrateFromChatId(self, val):
        self.migrate_from_chat_id = val

    # получение
    def getMigrateFromChatId(self):
        return self.migrate_from_chat_id


    # запись объекта класса Message
    def setPinnedMessage(self, val):
        self.pinned_message = Message(val)

    # получение объекта класса Message
    def getPinnedMessage(self):
        return self.pinned_message


    # запись объекта класса Invoice
    def setInvoice(self, val):
        self.invoice = Invoice(val)

    # получение объекта класса Invoice
    def getInvoice(self):
        return self.invoice


    # запись SuccessfulPayment
    def setSuccessfulPayment(self, val):
        self.successful_payment = SuccessfulPayment(val)

    # получение SuccessfulPayment
    def getSuccessfulPayment(self):
        return self.successful_payment


    # запись
    def setConnectedWebsite(self, val):
        self.connected_website = val

    # получение
    def  getConnectedWebsite(self):
        return self.connected_website


    # запись объекта класса PassportData
    def setPassportData(self, val):
        self.passport_data = PassportData(val)

    # получение объекта класса PassportData
    def getPassportData(self):
        return self.passport_data


    # запись InlineKeyboardMarkup
    def setReplyMarkup(self, val):
        self.reply_markup = InlineKeyboardMarkup(val)

    # получение InlineKeyboardMarkup
    def getReplyMarkup(self):
        return self.reply_markup



