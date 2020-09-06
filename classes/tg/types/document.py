from classes.tg.types.photoSize import PhotoSize
import json


class Document:
    'класс типов телеграм объектов'

    #	String	Identifier for this file, which can be used to download or reuse the file
    file_id = ""
    #	String	Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_unique_id = ""

    # объект класса PhotoSize	Optional. Thumbnail of the album cover to which the music file belongs
    thumb = None
    #	String	Optional. Original animation filename as defined by sender
    file_name = ""
    #	String	Optional. MIME type of the file as defined by sender
    mime_type = ""
    #	Integer	Optional. File size
    file_size = 0


    def __init__(self, obj):
        self.setFileId(obj['file_id'])
        self.setFileUniqueId(obj['file_unique_id'])

        if 'thumb' in obj:
            self.setThumb(obj['thumb'])
        if 'file_name' in obj:
            self.setFileName(obj['file_name'])
        if 'mime_type' in obj:
            self.setMimeType(obj['mime_type'])
        if 'file_size' in obj:
            self.setFileSize(obj['file_size'])


    def get(self):
        response = {
            'file_id':self.file_id,
            'file_unique_id':self.file_unique_id
        }

        if self.thumb is not None:
            response.update({'thumb':self.thumb.get()})
        if self.file_name != "":
            response.update({'file_name':self.file_name})
        if self.mime_type != "":
            response.update({'mime_type':self.mime_type})
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


    # запись объекта класса PhotoSize
    def setThumb(self, val):
        self.thumb = PhotoSize(val)

    # получение объекта класса PhotoSize
    def getThumb(self):
        return self.thumb


    # запись имени файла
    def setFileName(self, val):
        self.file_name = val

    # получение имени файла
    def getFileName(self):
        return self.file_name


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





