class StickerSet:
    'класс типов телеграм объектов'

    #	String	Sticker set name
    name = ""
    #	String	Sticker set title
    title = ""
    #	Boolean	True, if the sticker set contains animated stickers
    is_animated = False
    #	Boolean	True, if the sticker set contains masks
    contains_masks = False
    #	Array of Sticker	List of all set stickers
    stickers = []

    #	PhotoSize	Optional. Sticker set thumbnail in the .WEBP or .TGS format
    thumb = None


    def __init__(self, obj):
        self.setName(obj['name'])
        self.setTitle(obj['title'])
        self.setIsAnimated(obj['is_animated'])
        self.setContainsMasks(obj['contains_masks'])
        self.setStickers(obj['stickers'])

        if 'thumb' in obj:
            self.setThumb(obj['thumb'])


    # запись
    def setName(self, val):
        self.name = val

    # получение
    def getName(self):
        return self.name


    # запись
    def setTitle(self, val):
        self.title = val

    # получение
    def getTitle(self):
        return self.title


    # запись
    def setIsAnimated(self, val):
        self.is_animated = val

    # получение
    def setIsAnimated(self):
        return self.is_animated


    # запись
    def setContainsMasks(self, val):
        self.contains_masks = val

    # получение
    def getContainsMasks(self):
        return self.contains_masks


    # запись
    def setStickers(self, val):
        self.stickers = []
        i = 0
        while i < len(val):
            self.stickers.append(Sticker(val[i]))
            i += 1

    # получение
    def getStickers(self):
        return self.stickers


    # запись
    def setThumb(self, val):
        self.thumb = PhotoSize(val)

    # получение
    def getThumb(self):
        return self.thumb


