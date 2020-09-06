class ChatPhoto:
    'класс типов телеграм объектов'

    #	String	File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    small_file_id = ""

    #	String	Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    small_file_unique_id = ""

    #	String	File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    big_file_id = ""

    #	String	Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    big_file_unique_id = ""


    def __init__(self, obj):
        self.setSmallFileId(obj['small_file_id'])

        self.setSmallFileUniqueId(obj['small_file_unique_id'])

        self.setBigFileIid(obj['big_file_id'])

        self.setBigFileUniqueIid(obj['big_file_unique_id'])
    
    
    def get(self):
        response = {
            'small_file_id':self.small_file_id,
            'small_file_unique_id':self.small_file_unique_id,
            'big_file_id':self.big_file_id,
            'big_file_unique_id':self.big_file_unique_id
        }
        
        return response


    # запись малого идентификатора файла
    def setSmallFileId(self, val):
        self.small_file_id = val

    # получение малого идентификатора файла
    def getSmallFileId(self):
        return self.small_file_id


    # запись уникального малого идентификатора файла
    def setSmallFileUniqueId(self, val):
        self.small_file_unique_id = val

    # получение уникального малого идентификатора файла
    def getSmallFileUniqueId(self):
        return self.small_file_unique_id


    # запись большого идентификатора файла
    def setBigFileIid(self, val):
        self.big_file_id = val

    # получение большого идентификатора файла
    def getBigFileIid(self):
        return self.big_file_id


    # запись уникального большого идентификатора файла
    def setBigFileUniqueIid(self, val):
        self.big_file_unique_id = val

    # получение уникального большого идентификатора файла
    def getBigFileUniqueIid(self):
        return self.big_file_unique_id




