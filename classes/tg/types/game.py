from classes.tg.types.photoSize import PhotoSize
from classes.tg.types.messageEntity import MessageEntity
from classes.tg.types.animation import Animation

import json


class Game:
    'класс типов телеграм объектов'

    #	String	Title of the game
    title = ""
    #	String	Description of the game
    description = ""
    #	Array of PhotoSize	Photo that will be displayed in the game message in chats.
    photo = []

    #	String	Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    text = ""
    #	Array of MessageEntity	Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    text_entities = []
    #	Animation	Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
    animation = None


    def __init__(self, obj):
        self.setTitle(obj['title'])
        self.setDescription(obj['description'])
        self.setPhoto(obj['photo'])

        if 'text' in obj:
            self.setText(obj['text'])
        if 'text_entities' in obj:
            self.setTextEntities(obj['text_entities'])
        if 'animation' in obj:
            self.setAnimation(obj['animation'])


    def get(self):

        ph = []
        i = 0
        while i < len(self.photo):
            ph.append(self.photo[i].get())
            i += 1

        response = {
            'title':self.title,
            'description':self.description,
            'photo':ph
        }

        if self.text != "":
            response.update({'text':self.text})
        if self.text_entities != []:
            text_ent = []
            i = 0
            while i < len(self.text_entities):
                text_ent.append(self.text_entities[i].get())
                i += 1
            response.update({'text_entities':text_ent})
        if self.animation is not None:
            response.update({'animation':self.animation.get()})

        return response


    def getStr(self):
        return str(self.get())

    def getJson(self):
        return json.dumps(self.get())


    def setTitle(self, val):
        self.title = val

    def getTitle(self):
        return self.title


    def setDescription(self, val):
        self.description = val

    def getDescription(self):
        return self.description


    def setPhoto(self, val):
        self.photo = []
        i = 0
        while i < len(val):
            self.photo.append(PhotoSize(val[i]))
            i += 1

    def getPhoto(self):
        return self.photo


    def setText(self, val):
        self.text = val

    def getText(self):
        return self.text


    def setTextEntities(self, val):
        self.text_entities = []
        i = 0
        while i < len(val):
            self.text_entities.append(MessageEntity(val[i]))
            i += 1

    def getTextEntities(self):
        return self.text_entities


    def setAnimation(self, val):
        self.animation = Animation(val)

    def getAnimation(self):
        return self.animation


