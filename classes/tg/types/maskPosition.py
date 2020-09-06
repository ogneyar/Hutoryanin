import json


class MaskPosition:
    'класс типов телеграм объектов'

    #	String	The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
    point = ""
    #	Float number	Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    x_shift = 0
    #	Float number	Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    y_shift = 0
    #	Float number	Mask scaling coefficient. For example, 2.0 means double size.
    scale = 0


    def __init__(self, obj):
        self.setPoint(obj['point'])
        self.setXShift(obj['x_shift'])
        self.setYShift(obj['y_shift'])
        self.setScale(obj['scale'])


    def get(self):
        response = {
            'point':self.point,
            'x_shift':self.x_shift,
            'y_shift':self.y_shift,
            'scale':self.scale
        }
        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    # запись
    def setPoint(self, val):
        self.point = val

    # получение
    def getPoint(self):
        return self.point


    # запись
    def setXShift(self, val):
        self.x_shift = val

    # получение
    def getXShift(self):
        return self.x_shift


    # запись
    def setYShift(self, val):
        self.y_shift = val

    # получение
    def getYShift(self):
        return self.y_shift


    # запись
    def setScale(self, val):
        self.scale = val

    # получение
    def getScale(self):
        return self.scale


