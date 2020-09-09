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

token = os.getenv("TOKEN")
master = int(os.getenv("MASTER"))
debug = os.getenv("DEBUG")

groupHutor = -464572634 # group
groupHutor2 = -1001471520704 # supergroup
groupHutor3 = -1001393395949 # supergroup

testerBotoff = 351009636

# инициализация телеграм бота
tg = Bot(token)
try:

    update = None
    update = tg.start(request)

    if (text == "/start"):

        response = tg.sendMessage(chat_id, "Зачем жмёшь старт?")

    elif text == "":
        return HttpResponse("ok")


    else:
        if (chat_type == "private"):
            response = tg.sendMessage(chat_id, "Ха!")



except:
    return HttpResponse("ok")

return HttpResponse("ok")

