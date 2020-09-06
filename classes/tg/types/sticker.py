from classes.tg.types.photoSize import PhotoSize
from classes.tg.types.maskPosition import MaskPosition

import json


class Sticker:
    'класс типов телеграм объектов'

    #	String	Identifier for this file, which can be used to download or reuse the file
    file_id = ""
    #	String	Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_unique_id = ""
    #	Integer	Sticker width
    width = 0
    #	Integer	Sticker height
    height = 0
    #	Boolean	True, if the sticker is animated
    is_animated = False

    #	PhotoSize	Optional. Sticker thumbnail in the .WEBP or .JPG format
    thumb = None
    #	String	Optional. Emoji associated with the sticker
    emoji = ""
    #	String	Optional. Name of the sticker set to which the sticker belongs
    set_name = ""
    #	MaskPosition	Optional. For mask stickers, the position where the mask should be placed
    mask_position = None
    #	Integer	Optional. File size
    file_size = 0


    def __init__(self, obj):
        self.setFileId(obj['file_id'])
        self.setFileUniqueId(obj['file_unique_id'])
        self.setWidth(obj['width'])
        self.setHeight(obj['height'])
        self.setIsAnimated(obj['is_animated'])

        if 'thumb' in obj:
            self.setThumb(obj['thumb'])
        if 'emoji' in obj:
            self.setEmoji(obj['emoji'])
        if 'set_name' in obj:
            self.setSetName(obj['set_name'])
        if 'mask_position' in obj:
            self.setMaskPosition(obj['mask_position'])
        if 'file_size' in obj:
            self.setFileSize(obj['file_size'])


    def get(self):
        response = {
            'file_id':self.file_id,
            'file_unique_id':self.file_unique_id,
            'width':self.width,
            'height':self.height,
            'is_animated':self.is_animated
        }

        if self.thumb is not None:
            response.update({'thumb':self.thumb.get()})
        if self.emoji != "":
            response.update({'emoji':self.emoji})
        if self.set_name != "":
            response.update({'set_name':self.set_name})
        if self.mask_position is not None:
            response.update({'mask_position':self.mask_position.get()})
        if self.file_size != 0:
            response.update({'file_size':self.file_size})

        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    # запись id
    def setFileId(self, val):
        self.file_id = val

    # получение id
    def getFileId(self):
        return self.file_id


    # запись id
    def setFileUniqueId(self, val):
        self.file_unique_id = val

    # получение id
    def getFileUniqueId(self):
        return self.file_unique_id


    # запись
    def setWidth(self, val):
        self.width = val

    # получение
    def getWidth(self):
        return self.width


    # запись
    def setHeight(self, val):
        self.height = val

    # получение
    def getHeight(self):
        return self.height


    # запись
    def setIsAnimated(self, val):
        self.is_animated = val

    # получение
    def getIsAnimated(self):
        return self.is_animated


    # запись
    def setThumb(self, val):
        self.thumb = PhotoSize(val)

    # получение
    def getThumb(self):
        return self.thumb


    # запись
    def setEmoji(self, val):
        self.emoji = val

    # получение
    def getEmoji(self):
        return self.emoji


    # запись
    def setSetName(self, val):
        self.set_name = val

    # получение
    def getSetName(self):
        return self.set_name


    # запись
    def setMaskPosition(self, val):
        self.mask_position = MaskPosition(val)

    # получение
    def getMaskPosition(self):
        return self.mask_position


    # запись размера файла
    def setFileSize(self, val):
        self.file_size = val

    # получение размера файла
    def getFileSize(self):
        return self.file_size




