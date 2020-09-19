from django.http import HttpResponse

import os, bmemcached, requests
from bs4 import BeautifulSoup

from classes.tg.botApi import Bot

mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')
mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
mc.enable_retry_delay(True)

token = os.getenv("TOKEN")
master = int(os.getenv("MASTER"))
tg = Bot(token)

debug = os.getenv("DEBUG")
groupHutor = -464572634 # group
groupHutor2 = -1001471520704 # supergroup
groupHutor3 = -1001393395949 # supergroup
testerBotoff = 351009636
inline_keyboard_markup = {
    'inline_keyboard':[
        [
            {'text':'Сайт ХуторянинЪ','url':'https://hutoryanin.ru'}
        ],
        [
            {'text':'Ссылка на соц.сети','url':'https://t.me/hutoryanin_chat/271'}
        ]
    ]
}


class CallBack:

    def __init__(self, callback_query):

        try:
            id = callback_query.getId()
            callback_from = callback_query.getFrom()
            data= callback_query.getData()

            if data is None:
                return HttpResponse("ok")

            if data == "public":

                url = mc.get("url")
                title = mc.get("title")
                # формирование публикации
                caption = "Здравствуйте все! 🤚\n\n"
                caption += "Вышло новое видео на ютуб-канале [ХуторянинЪ.](https://www.youtube.com/c/ХуторянинЪ) "
                caption += "*" + title + "*\n\n"
                caption += "Смотрите, комментируйте, ставьте лайки, подписывайтесь на канал.\n*Приятного просмотра!* 😉\n"

                text_url = "\n[СМОТРЕТЬ ЭТО ВИДЕО!](" + url + ")"
                text_url = text_url * 3

                tg.sendPhoto(master, mc.get("file_id"), caption + text_url, "markdown", reply_markup=inline_keyboard_markup)

                mc.delete("file_id")
                mc.delete("url")
                mc.delete("file_id")


            elif data == "delete":

                mc.delete("file_id")
                mc.delete("url")
                mc.delete("file_id")

                tg.sendMessage(master, "Очистил memcached")

        except:

            return HttpResponse("ok")


        return HttpResponse("ok")


