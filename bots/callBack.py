from django.http import HttpResponse

from web.models import Url

import os, bmemcached, requests
from bs4 import BeautifulSoup

from classes.tg.botApi import Bot

from web.models import Url
from web.forms import UrlForm


mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')
mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
mc.enable_retry_delay(True)

token = os.getenv("TOKEN")
master = os.getenv("MASTER")
if master is not None:
    master = int(master)
tg = Bot(token)

debug = os.getenv("DEBUG")
groupHutor = -464572634 # group
groupHutor2 = -1001471520704 # supergroup
groupHutor3 = -1001393395949 # supergroup
tg_channel = os.getenv("CHANNEL") # channel
testerBotoff = 351009636
inline_keyboard_markup = {
    'inline_keyboard':[
        '''
        [
            {'text':'Сайт ХуторянинЪ','url':'https://hutoryanin.ru'}
        ],
        '''
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
            data = callback_query.getData()

            if data is None:
                return HttpResponse("ok")

            #tg.answerCallbackQuery(id)

            if data == "public":

                url = mc.get("url")
                title = mc.get("title")
                file_id = mc.get("file_id")

                # формирование публикации
                caption = "Здравствуйте все! 🤚\n\n"
                caption += "Вышло новое видео на ютуб-канале [ХуторянинЪ.](https://www.youtube.com/c/ХуторянинЪ) "
                caption += "*" + title + "*\n\n"
                caption += "Смотрите, комментируйте, ставьте лайки, подписывайтесь на канал.\n*Приятного просмотра!* 😉\n"

                text_url = "\n[СМОТРЕТЬ ЭТО ВИДЕО!](" + url + ")"
                text_url = text_url * 3

                tg.sendPhoto(master, file_id, caption + text_url, "markdown", reply_markup=inline_keyboard_markup)

                data = {
                    'title':title,
                    'url':url,
                    'file_id':file_id
                }
                form = UrlForm(data)
                if form.is_valid():
                    form.save()
                    #tg.sendMessage(master, "Сохранил в БД.")
                    tg.sendPhoto(tg_channel, file_id, caption + text_url, "markdown", reply_markup=inline_keyboard_markup)
                    tg.answerCallbackQuery(id, "Опубликовал на канале и сохранил в БД!", True)
                else:
                    tg.answerCallbackQuery(id, "Форма не валидная!", True)

                mc.delete("wait")
                mc.delete("file_id")
                mc.delete("url")
                mc.delete("title")


            elif data == "delete":

                mc.delete("wait")
                mc.delete("file_id")
                mc.delete("url")
                mc.delete("title")

                tg.sendMessage(master, "Очистил memcached")

        except:

            return HttpResponse("ok")


        return HttpResponse("ok")


