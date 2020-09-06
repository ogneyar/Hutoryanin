from classes.tg.types.photoSize import PhotoSize
import json


class VideoNote:
    'класс типов телеграм объектов'

    # String	Identifier for this file, which can be used to download or reuse the file
    file_id = ""
    # String	Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_unique_id = ""
    # Integer	Length of the entity in UTF-16 code units
    length = 0
    # Integer	Duration of the audio in seconds as defined by sender
    duration = 0

    # объект класса PhotoSize	Optional. Thumbnail of the album cover to which the music file belongs
    thumb = None
    # Integer	Optional. File size
    file_size = 0


    def __init__(self, obj):
        self.setFileId(obj['file_id'])
        self.setFileUniqueId(obj['file_unique_id'])
        self.setLength(obj['length'])
        self.setDuration(obj['duration'])

        if 'thumb' in obj:
            self.setThumb(obj['thumb'])
        if 'file_size' in obj:
            self.setFileSize(obj['file_size'])


    def get(self):
        response = {
            'file_id':self.file_id,
            'file_unique_id':self.file_unique_id,
            'length':self.length,
            'duration':self.duration
        }

        if self.thumb is not None:
            response.update({'thumb':self.thumb.get()})
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


    #
    def setLength(self, val):
        self.length = val

    def getLength(self):
        return self.length


    # запись
    def setDuration(self, val):
        self.duration = val

    # получение
    def getDuration(self):
        return self.duration


    # запись объекта класса PhotoSize
    def setThumb(self, val):
        self.thumb = PhotoSize(val)

    # получение объекта класса PhotoSize
    def getThumb(self):
        return self.thumb


    # запись размера файла
    def setFileSize(self, val):
        self.file_size = val

    # получение размера файла
    def getFileSize(self):
        return self.file_size



