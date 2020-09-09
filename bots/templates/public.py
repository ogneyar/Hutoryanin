from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import requests
import json
import os
from bs4 import BeautifulSoup
import bmemcached

from classes.tg.botApi import Bot
from classes.tg.types.replyKeyboardMarkup import ReplyKeyboardMarkup
from classes.tg.types.chatPermissions import ChatPermissions


mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')

mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
mc.enable_retry_delay(True)


def bot(request):
    try:
        if (request.method == "POST"):

            token = os.getenv("TOKEN")
            master = int(os.getenv("MASTER"))
            debug = os.getenv("DEBUG")

            groupHutor = -464572634 # group
            groupHutor2 = -1001471520704 # supergroup
            groupHutor3 = -1001393395949 # supergroup

            testerBotoff = 351009636

            # инициализация телеграм бота
            tg = Bot(token)

            if (debug == "Да"):
                response = tg.sendMessage(master, request.body, disable_web_page_preview=True)
                #return HttpResponse("ok")

            update = None
            update = tg.start(request)

            if (debug == "Да"):
                response = tg.sendMessage(master, update.getStr(), disable_web_page_preview=True)

            message = update.getMessage()
            if message is None:
                editedMessage = update.getEditedMessage()
                message = editedMessage

            if message is None:
                channelPost = update.getChannelPost()
                message = channelPost

            if message is None:
                editedChannelPost = update.getEditedChannelPost()
                message = editedChannelPost

            if message is None:
                poll = update.getPoll()
                if poll is None:
                    response = tg.sendMessage(master, "message,  channelPost and Poll is None")
                else:
                    response = tg.sendMessage(master, "This update is Poll")

                return HttpResponse("ok")

            new_chat_members = message.getNewChatMembers()
            if new_chat_members != []:
                new_chat_members_from_is_bot = new_chat_members[0].getIsBot()
            else:
                new_chat_members_from_is_bot = False
            message_id = message.getMessageId()
            text = message.getText()
            #video_note = message.getVideoNote()

            message_from = message.getFrom()
            if message_from is not None:
                from_id = message_from.getId()
                from_first_name = message_from.getFirstName()
                from_is_bot = message_from.getIsBot()
            else:
                from_id = 0
                from_first_name = "unknown"
                from_is_bot = False

            chat = message.getChat()
            chat_id = chat.getId()
            chat_type = chat.getType()
            chat_title = chat.getTitle()
            if chat_title == "":
                chat_title = "НЕИЗВЕСТНО"


            if (text == "/start"):

                response = tg.sendMessage(chat_id, "Зачем жмёшь старт?")





            elif text == "":
                return HttpResponse("ok")


            else:
                if (chat_type == "private"):
                    response = tg.sendMessage(chat_id, "Ха!")



    except Exception:
        return HttpResponse("ok")

    return HttpResponse("ok")

