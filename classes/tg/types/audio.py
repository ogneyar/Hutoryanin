from classes.tg.types.photoSize import PhotoSize
import json


class Audio:
    'класс типов телеграм объектов'

    #	String	Identifier for this file, which can be used to download or reuse the file
    file_id = ""
    #	String	Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_unique_id = ""
    #	Integer	Duration of the audio in seconds as defined by sender
    duration = 0

    #	String	Optional. Performer of the audio as defined by sender or by audio tags
    performer = ""
    #	String	Optional. Title of the audio as defined by sender or by audio tags
    title = ""
    #	String	Optional. MIME type of the file as defined by sender
    mime_type = ""
    #	Integer	Optional. File size
    file_size = 0
    # объект класса PhotoSize	Optional. Thumbnail of the album cover to which the music file belongs
    thumb = None


    def __init__(self, obj):
        self.setFileId(obj['file_id'])
        self.setFileUniqueId(obj['file_unique_id'])
        self.setDuration(obj['duration'])

        if 'performer' in obj:
            self.setPerformer(obj['performer'])
        if 'title' in obj:
            self.setTitle(obj['title'])
        if 'mime_type' in obj:
            self.setMimeType(obj['mime_type'])
        if 'file_size' in obj:
            self.setFileSize(obj['file_size'])
        if 'thumb' in obj:
            self.setThumb(obj['thumb'])


    def get(self):
        response = {
            'file_id':self.file_id,
            'file_unique_id':self.file_unique_id,
            'duration':self.duration
        }

        if self.performer != "":
            response.update({'performer':self.performer})
        if self.title != "":
            response.update({'title':self.title})
        if self.mime_type != "":
            response.update({'mime_type':self.mime_type})
        if self.file_size != 0:
            response.update({'file_size':self.file_size})
        if self.thumb is not None:
            response.update({'thumb':self.thumb.get()})

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
    def setDuration(self, val):
        self.duration = val

    # получение
    def getDuration(self):
        return self.duration


    # запись
    def setPerformer(self, val):
        self.performer = val

    # получение
    def getPerformer(self):
        return self.performer


    # запись заголовка
    def setTitle(self, val):
        self.title = val

    # получение заголовка
    def getTitle(self):
        return self.title


    # запись стандарта, описывающего передачу различных типов данных
    def setMimeType(self, val):
        self.mime_type = val

    # получение стандарта, описывающего передачу различных типов данных
    def getMimeType(self):
        return self.mime_type


    # запись размера файла
    def setFileSize(self, val):
        self.file_size = val

    # получение размера файла
    def getFileSize(self):
        return self.file_size


    # запись объекта класса PhotoSize
    def setThumb(self, val):
        self.thumb = PhotoSize(val)

    # получение объекта класса PhotoSize
    def getThumb(self):
        return self.thumb




