class UserProfilePhotos:
    'класс типов телеграм объектов'

    # Integer	Total number of profile pictures the target user has
    total_count = 0
    # Array of Array of PhotoSize	Requested profile pictures (in up to 4 sizes each)
    photos = []

    def __init__(self, obj):
        self.setTotalCount(obj['total_count'])
        self.setPhotos(obj['photos'])


    # запись
    def setTotalCount(self, val):
        self.total_count = val

    # получение
    def getTotalCount(self):
        return self.total_count


    # запись
    def setPhotos(self, val):
        self.photos = []
        arr = []
        i = 0
        j = 0
        while i < len(val):
            while j < len(val[i]):
                arr.append(PhotoSize(val[i][j]))
                j += 1
            self.photos.append(arr)
            j = 0
            i += 1
            arr = []

    # получение
    def getPhotos(self):
        return self.photos


