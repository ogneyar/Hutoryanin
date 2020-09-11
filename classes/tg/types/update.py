from classes.tg.types.message import Message
from classes.tg.types.inlineQuery import InlineQuery
from classes.tg.types.chosenInlineResult import ChosenInlineResult
from classes.tg.types.callbackQuery import CallbackQuery
from classes.tg.types.shippingQuery import ShippingQuery
from classes.tg.types.preCheckoutQuery import PreCheckoutQuery
from classes.tg.types.poll import Poll
from classes.tg.types.pollAnswer import PollAnswer

import json


class Update:
    'телеграм объект типа Update'

    # целочисленный тип данных int
    update_id = 0

    # объект класса Message (Optional)
    message = None
    # объект класса Message (Optional)
    edited_message = None
    # объект класса Message (Optional)
    channel_post = None
    # объект класса Message (Optional)
    edited_channel_post = None
    # объект класса InlineQuery (Optional)
    inline_query = None
    # объект класса ChosenInlineResult (Optional)
    chosen_inline_result = None
    # объект класса CallbackQuery (Optional)
    callback_query = None
    # объект класса ShippingQuery (Optional)
    shipping_query = None
    # объект класса PreCheckoutQuery (Optional)
    pre_checkout_query = None
    # объект класса Poll (Optional)
    poll = None
    # объект класса PollAnswer (Optional)
    poll_answer = None


    # конструктор
    def __init__(self, obj):
        self.setUpdateId(obj['update_id'])
        if 'message' in obj:
            self.setMessage(obj['message'])
        if 'edited_message' in obj:
            self.setEditedMessage(obj['edited_message'])
        if 'channel_post' in obj:
            self.setChannelPost(obj['channel_post'])
        if 'edited_channel_post' in obj:
            self.setEditedChannelPost(obj['edited_channel_post'])
        if 'inline_query' in obj:
            self.setInlineQuery(obj['inline_query'])
        if 'chosen_inline_result' in obj:
            self.setChosenInlineResult(obj['chosen_inline_result'])
        if 'callback_query' in obj:
            self.setCallbackQuery(obj['callback_query'])

        '''
        if 'shipping_query' in obj:
            self.setShippingQuery(obj['shipping_query'])
        if 'pre_checkout_query' in obj:
            self.setPreCheckoutQuery(obj['pre_checkout_query'])
        '''

        if 'poll' in obj:
            self.setPoll(obj['poll'])
        if 'poll_answer' in obj:
            self.setPollAnswer(obj['poll_answer'])


    def get(self):
        response = {
            'update_id':self.update_id
        }
        if self.message is not None:
            response.update({'message':self.message.get()})
        if self.edited_message is not None:
            response.update({'edited_message':self.edited_message.get()})
        if self.channel_post is not None:
            response.update({'channel_post':self.channel_post.get()})
        if self.edited_channel_post is not None:
            response.update({'edited_channel_post':self.edited_channel_post.get()})
        '''
        if self.inline_query is not None:
            response.update({'inline_query':self.inline_query.get()})
        if self.chosen_inline_result is not None:
            response.update({'chosen_inline_result':self.chosen_inline_result.get()})
        if self.callback_query is not None:
            response.update({'callback_query':self.callback_query.get()})
        if self.shipping_query is not None:
            response.update({'shipping_query':self.shipping_query.get()})
        if self.pre_checkout_query is not None:
            response.update({'pre_checkout_query':self.pre_checkout_query.get()})
        if self.poll is not None:
            response.update({'poll':self.poll.get()})
        if self.poll_answer is not None:
            response.update({'poll_answer':self.poll_answer.get()})
        '''

        return response


    def getStr(self):
        return str(self.get())


    def getJson(self):
        return json.dumps(self.get())


    # запись id обновления
    def setUpdateId(self, updId):
        self.update_id = updId

    # получение id обновления
    def getUpdateId(self):
        return self.update_id


    # запись объекта класса Message
    def setMessage(self, msg):
        self.message = Message(msg)

    # получение объекта класса Message
    def getMessage(self):
        return self.message


    # запись объекта класса Message
    def setEditedMessage(self, msg):
        self.edited_message = Message(msg)

    # получение объекта класса Message
    def getEditedMessage(self):
        return self.edited_message


    # запись объекта класса Message
    def setChannelPost(self, msg):
        self.channel_post = Message(msg)

    # получение объекта класса Message
    def getChannelPost(self):
        return self.channel_post


    # запись объекта класса Message
    def setEditedChannelPost(self, msg):
        self.edited_channel_post = Message(msg)

    # получение объекта класса Message
    def getEditedChannelPost(self):
        return self.edited_channel_post


    # запись объекта класса InlineQuery
    def setInlineQuery(self, val):
        self.inline_query = InlineQuery(val)

    # получение объекта класса InlineQuery
    def getInlineQuery(self):
        return self.inline_query


    # запись объекта класса ChosenInlineResult
    def setChosenInlineResult(self, val):
        self.chosen_inline_result = ChosenInlineResult(val)

    # получение объекта класса ChosenInlineResult
    def getChosenInlineResult(self):
        return self.chosen_inline_result


    # запись объекта класса CallbackQuery
    def setCallbackQuery(self, val):
        self.callback_query = CallbackQuery(val)

    # получение объекта класса CallbackQuery
    def getCallbackQuery(self):
        return self.callback_query


    # запись объекта класса ShippingQuery
    #def setShippingQuery(self, val):
    #    self.shipping_query = ShippingQuery(val)

    # получение объекта класса ShippingQuery
    #def getShippingQuery(self):
    #    return self.shipping_query


    # запись объекта класса PreCheckoutQuery
    #def setPreCheckoutQuery(self, val):
    #    self.pre_checkout_query = PreCheckoutQuery(val)

    # получение объекта класса PreCheckoutQuery
    #def getPreCheckoutQuery(self):
    #    return self.pre_checkout_query


    # запись объекта класса Poll
    def setPoll(self, val):
        self.poll = Poll(val)

    # получение объекта класса Poll
    def getPoll(self):
        return self.poll


    # запись объекта класса PollAnswer
    def setPollAnswer(self, val):
        self.poll_answer = PollAnswer(val)

    # получение объекта класса PollAnswer
    def getPollAnswer(self):
        return self.poll_answer




