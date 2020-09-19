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
inline_keyboard_markup_finish = {
    'inline_keyboard':[
        [
            {'text':'Сайт ХуторянинЪ','url':'https://hutoryanin.ru'}
        ],
        [
            {'text':'Ссылка на соц.сети','url':'https://t.me/hutoryanin_chat/271'}
        ]
    ]
}
inline_keyboard_markup = {
    'inline_keyboard':[
        [
            {'text':'Опубликовать','callback_data':'public'}
        ],
        [
            {'text':'Сайт ХуторянинЪ','url':'https://hutoryanin.ru'}
        ],
        [
            {'text':'Ссылка на соц.сети','url':'https://t.me/hutoryanin_chat/271'}
        ],
        [
            {'text':'Удалить','callback_data':'delete'}
        ],
    ]
}


class Public:

    def __init__(self, message):

        try:
            message_id = message.getMessageId()
            text = message.getText()
            photo= message.getPhoto()

            if mc.get("wait") == "markdown":

                tg.sendMessage(master, text, "markdown", True)
                mc.delete("wait")

                tg.sendMessage(master, "Готово.")


            elif mc.get("wait") == "photo":
                if photo != []:
                    file_id = photo[2].getFileId()
                    tg.sendPhoto(master, file_id, reply_markup=inline_keyboard_markup_finish)
                    mc.set("wait", "url")
                    mc.set("file_id", file_id)
                    tg.sendMessage(master, "Пришли ссылку на видео.")
                else:
                    tg.sendMessage(master, "Нужно фото, в формате .jpg")


            elif mc.get("wait") == "url":
                # получение названия публикации с помощью парсинга сайта
                headers = {
                    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106",
                    'x-youtube-client-name': '1',
                    'x-youtube-client-version': '2.20200529.02.01'
                }
                url = text
                page = requests.get(url, headers=headers)
                soup = BeautifulSoup(page.text, "lxml")
                full_title = str(soup.title.get_text())
                num = full_title.find(" - YouTube")
                title = full_title[:num]
                # формирование публикации
                caption = "Здравствуйте все! 🤚\n\n"
                caption += "Вышло новое видео на ютуб-канале [ХуторянинЪ.](https://www.youtube.com/c/ХуторянинЪ) "
                caption += "*" + title + "*\n\n"
                caption += "Смотрите, комментируйте, ставьте лайки, подписывайтесь на канал.\n*Приятного просмотра!* 😉\n"

                text_url = "\n[СМОТРЕТЬ ЭТО ВИДЕО!](" + url + ")"
                text_url = text_url * 3

                tg.sendPhoto(master, mc.get("file_id"), caption + text_url, "markdown", reply_markup=inline_keyboard_markup)

                mc.set("url", url)
                mc.set("title", title)

                mc.delete("wait")


        except:
            mc.delete("wait")
            mc.delete("file_id")
            mc.delete("url")
            mc.delete("title")


        return HttpResponse("ok")


