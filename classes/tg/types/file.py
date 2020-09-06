class File:
    'класс типов телеграм объектов'

    #	String	Identifier for this file, which can be used to download or reuse the file
    file_id = ""
    #	String	Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_unique_id = ""

    #	Integer	Optional. File size, if known
    file_size = 0
    #	String	Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    file_path = ""


    def __init__(self, obj):
        self.setFileId(obj['file_id'])
        self.setFileUniqueId(obj['file_unique_id'])

        if 'file_size' in obj:
            self.setFileSize(obj['file_size'])
        if 'file_path' in obj:
            self.setFilePath(obj['file_path'])



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


    # запись размера файла
    def setFileSize(self, val):
        self.file_size = val

    # получение размера файла
    def getFileSize(self):
        return self.file_size


    # запись
    def setFilePath(self, val):
        self.file_path = val

    # получение
    def getFilePath(self):
        return self.file_path


