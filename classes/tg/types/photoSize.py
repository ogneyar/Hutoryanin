class PhotoSize:
    'класс типов телеграм объектов'


    # String	Identifier for this file, which can be used to download or reuse the file
    file_id = ""
    # String	Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_unique_id = ""
    # Integer	Photo width
    width = 0
    # Integer	Photo height
    height = 0

    # Integer	Optional. File size
    file_size = 0


    # конструктор
    def __init__(self, obj):
        self.setFileId(obj['file_id'])
        self.setFileUniqueId(obj['file_unique_id'])
        self.setWidth(obj['width'])
        self.setHeight(obj['height'])

        if 'file_size' in obj:
            self.setFileSize(obj['file_size'])


    def get(self):
        response = {
            'file_id':self.file_id,
            'file_unique_id':self.file_unique_id,
            'width':self.width,
            'height':self.height
        }
        if self.file_size != 0:
            response.update({'file_size':self.file_size})

        return response


    #
    def setFileId(self, val):
        self.file_id = val

    def getFileId(self):
        return self.file_id


    #
    def setFileUniqueId(self, val):
        self.file_unique_id = val

    def getFileUniqueId(self):
        return self.file_unique_id


    #
    def setWidth(self, val):
        self.width = val

    def getWidth(self):
        return self.width


    #
    def setHeight(self, val):
        self.height = val

    def getHeight(self):
        return self.height


    #
    def setFileSize(self, val):
        self.file_size = val

    def getFileSize(self):
        return self.file_size


