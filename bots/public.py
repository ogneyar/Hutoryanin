from django.http import HttpResponse

import os, bmemcached, requests
from bs4 import BeautifulSoup

from classes.tg.botApi import Bot

class Public:

    def __init__(self, message):

        try:

            mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
            mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
            mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')
            token = os.getenv("TOKEN")
            master = int(os.getenv("MASTER"))
            debug = os.getenv("DEBUG")
            groupHutor = -464572634 # group
            groupHutor2 = -1001471520704 # supergroup
            groupHutor3 = -1001393395949 # supergroup
            testerBotoff = 351009636
            message_id = message.getMessageId()
            text = message.getText()
            photo= message.getPhoto()
            inline_keyboard_markup = {
                'inline_keyboard':[
                    #[
                    #    {'text':'Сайт ХуторянинЪ','url':'https://hutoryanin.herokuapp.com'}
                    #],
                    [
                        {'text':'Ссылка на соц.сети','url':'https://t.me/hutoryanin_chat/271'}
                    ]
                ]
            }

            mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
            mc.enable_retry_delay(True)

            # инициализация телеграм бота
            tg = Bot(token)

            if mc.get("wait") == "markdown":

                response = tg.sendMessage(master, text, "markdown", True)
                mc.delete("wait")

                response = tg.sendMessage(master, "Готово.")


            elif mc.get("wait") == "photo":
                if photo != []:
                    file_id = photo[2].getFileId()
                    response = tg.sendPhoto(master, file_id, mc.get("url"), reply_markup=inline_keyboard_markup)
                    mc.set("wait", "url")
                    mc.set("file_id", file_id)
                    response = tg.sendMessage(master, "Пришли ссылку на видео.")
                else:
                    response = tg.sendMessage(master, "Нужно фото, в формате .jpg")


            elif mc.get("wait") == "url":

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

                caption = "Здравствуйте все! 🤚\n\n"
                caption += "Вышло новое видео на ютуб-канале [ХуторянинЪ](https://www.youtube.com/c/ХуторянинЪ). "
                caption += "*" + title + "*\n\n"
                caption += "Смотрите, комментируйте, ставьте лайки, подписывайтесь на канал.\n*Приятного просмотра!* 😉\n"

                text_url = "\n[СМОТРЕТЬ ЭТО ВИДЕО!](" + text + ")"
                text_url = text_url * 3

                response = tg.sendPhoto(master, mc.get("file_id"), caption + text_url, "markdown", reply_markup=inline_keyboard_markup)


                response = tg.sendMessage(master, "Всё.")
                mc.delete("wait")

                mc.delete("file_id")


            elif mc.get("wait") == "description":
                pass


            else:
                response = tg.sendMessage(master, "Произошла ошибка!")
                mc.delete("wait")
                mc.delete("file_id")

        except:

            mc.delete("wait")
            mc.delete("file_id")

            return HttpResponse("ok")


        return HttpResponse("ok")


