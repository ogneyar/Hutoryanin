from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import include

import requests, json, os, bmemcached
from bs4 import BeautifulSoup

from bots.public import Public
from bots.callBack import CallBack

from classes.tg.botApi import Bot
from classes.tg.types.replyKeyboardMarkup import ReplyKeyboardMarkup
from classes.tg.types.chatPermissions import ChatPermissions


mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')

mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
mc.enable_retry_delay(True)

token = os.getenv("TOKEN")
master = os.getenv("MASTER")
if master is not None:
    master = int(master)
debug = os.getenv("DEBUG")

groupHutor = -1001476461678 # supergroup
groupHutor2 = -1001471520704 # supergroup
groupHutor3 = -1001393395949 # supergroup

tg_channel = os.getenv("CHANNEL") # channel

testerBotoff = 351009636

# инициализация телеграм бота
tg = Bot(token)


def bot(request):
    try:
        if (request.method == "POST"):

            # if (debug == "Да"):
                # tg.sendMessage(master, request.body, disable_web_page_preview=True)
                # return HttpResponse("ok")

            update = None
            update = tg.start(request)

            if (debug == "Да"):
                tg.sendMessage(master, update.getStr(), disable_web_page_preview=True)

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
                callback_query = update.getCallbackQuery()

                if callback_query is None:

                    poll = update.getPoll()
                    if poll is None:
                        tg.sendMessage(master, "message,  channelPost and Poll is None")
                    else:
                        tg.sendMessage(master, "This update is Poll")

                else:
                    CallBack(callback_query)

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

            help_list = "Список методов API Telegram (1):\n\n"
            help_list += "/sendMessage - отправка сообщения\n\n"
            help_list += "/forwardMessage - пересылка\n\n"
            help_list += "/editMessageText - изменение сообщения\n\n"
            help_list += "/deleteMessage - удаление сообщения\n\n"
            help_list += "/reply_keyboard_markup - кнопки\n\n"
            help_list += "/reply_keyboard_remove - удаление кнопок\n\n"
            help_list += "/inline_keyboard_markup - кнопки на сообщении\n\n"
            help_list += "/sendPhoto - отправка фото\n\n"
            help_list += "/sendAudio отправка звука\n\n"
            help_list += "/sendDocument - отправка документа\n\n"
            help_list += "/sendVideo - отправка видео\n\n"
            help_list += "/sendAnimation отправка анимации\n\n"
            help_list += "/sendVoice - голосовое сообщение\n\n"
            help_list += "/sendVideoNote - видео в круге\n\n"
            help_list += "/sendMediaGroup - группа фото\n\n"
            help_list += "/sendLocation - отправка локации\n\n"
            help_list += "/editMessageLiveLocation - изменение локации\n\n"
            help_list += "/stopMessageLiveLocation - запрет изменения локации\n\n"
            help_list += "/sendVenue - отправка места встречи\n\n"
            help_list += "/sendContact - отправка контакта\n\n"
            help_list += "/sendPoll - отправка опроса\n\n"
            help_list += "/sendDice - игральная кость\n\n"
            help_list += "/sendChatAction - показать действия бота\n\n"
            help_list += "/getUserProfilePhotos - возвращает фото профиля\n\n"
            help_list += "/getFile - информация о файле\n\n"

            help_list += "------------\n\n"
            help_list += "/methods_two\n\n"


            help_list2 = "Список методов API Telegram (2):\n\n"
            help_list2 += "/kickChatMember - удаление пользователя из группы(канала)\n\n"
            help_list2 += "/unbanChatMember - снятие БАНа с пользователя\n\n"
            help_list2 += "/restrictChatMember - установка разрешений пользователя\n\n"
            help_list2 += "\n\nWhere /promoteChatMember???\n\n"


            help_list2 += "------------\n\n"
            help_list2 += "/methods_one\n\n"

            keyboard = [[{'text':'Ссылка на PRIZMarket', 'url':'https://prizmarket.ru'}]]
            markup = {'inline_keyboard':keyboard}

            help = "Выбери один из списков методов Telegram API:\n\n/methods_one\n\n/methods_two"


            if (mc.get("wait") is not None) and (chat_id == master):
                #tg.sendMessage(chat_id, "Подключил файл")
                return Public(message)


            if (text == "/start"):
                if chat_id == master:
                    reply_keyboard_markup = {
                        'keyboard':[
                            [
                                {'text':'Публикация'},
                                {'text':'Cсылкодел'}
                            ],
                            [
                                {'text':'Скрыть'}
                            ]
                        ],
                        'resize_keyboard':True
                    }
                    tg.sendMessage(chat_id, "Здравствуй *Мастер*!\n\nЖми /help, если надо.", "markdown", reply_markup=reply_keyboard_markup)
                else:
                    tg.sendMessage(chat_id, "Здравствуй *" + from_first_name + "*!\n\nЖми /help", "markdown")


            elif (text == "Публикация" and chat_id == master):

                tg.sendMessage(chat_id, "Пришли фото новой публикации.")

                mc.set("wait", "photo")


            elif (text == "Cсылкодел" and chat_id == master):

                tg.sendMessage(chat_id, "Пришли текст в стиле markdown.")

                mc.set("wait", "markdown")


            elif (text == "тест"):

                yourArray = givMeArray([[1,2,3],[4,5,6],[7,8,9]])
                tg.sendMessage(chat_id, "Вот: " + str(yourArray))

                '''
            elif (text == "ы" and chat_id == master):

                if mc.get("wait") is not None:
                    if mc.get("wait") == "test":
                        tg.sendMessage(chat_id, "Принял 'ы'.")
                        mc.delete("wait")

                else:
                    tg.sendMessage(chat_id, "Чего?")
                '''


            elif (text == "/help"):

                tg.sendMessage(chat_id, help)


            elif (text == "/methods_one"):

                tg.sendMessage(chat_id, help_list)


            elif (text == "/methods_two"):

                tg.sendMessage(chat_id, help_list2)


            elif (text == "/sendMessage"):

                tg.sendMessage(chat_id, "Обычное сообщение.")


            elif (text == "/forwardMessage"):

                tg.forwardMessage(chat_id, chat_id, message_id)
                tg.sendMessage(chat_id, "Сообщение переслано.")


            elif (text == "/editMessageText"):

                response = tg.sendMessage(chat_id, "Смотри на этот текст")
                tg.sendMessage(chat_id, "Смотри на этот текст")
                tg.sendMessage(chat_id, "Смотри на этот текст")

                result = tg.editMessageText(chat_id, response['message_id'], "Видишь?")
                response = tg.sendMessage(chat_id, "Сообщение изменено.")


            elif (text == "/deleteMessage"):

                tg.deleteMessage(chat_id, message_id)
                tg.sendMessage(chat_id, "Сообщение удалено.")


            elif (text == "/reply_keyboard_markup"):
                '''
                reply_keyboard_markup = {
                    'keyboard':[
                        [
                            {'text':'Кнопа1'},
                            {'text':'Кнопа2'}
                        ],
                        [
                            {'text':'Кнопа3'}
                        ]
                    ],
                    'resize_keyboard':True
                }
                '''
                keyboard_button1 = {'text':'Кнопа1'}
                keyboard_button2 = {'text':'Кнопа2'}
                keyboard_button3 = {'text':'Кнопа3'}
                keyboard_line1 = []
                keyboard_line2 = []
                keyboard_line1.append(keyboard_button1)
                keyboard_line1.append(keyboard_button2)
                keyboard_line2.append(keyboard_button3)
                keyboard_markup = []
                keyboard_markup.append(keyboard_line1)
                keyboard_markup.append(keyboard_line2)
                reply_keyboard_markup = {}
                reply_keyboard_markup.update({'keyboard':keyboard_markup})
                reply_keyboard_markup.update({'resize_keyboard':True})

                tg.sendMessage(chat_id, "Кнопки добавленны.", "markdown", True, None, 0, reply_keyboard_markup)


            elif (text == "/reply_keyboard_remove" or text == "Скрыть"):

                reply_keyboard_remove = {'remove_keyboard':True}
                tg.sendMessage(chat_id, "Кнопки удалены.", reply_markup=reply_keyboard_remove)


            elif (text == "/inline_keyboard_markup"):
                '''
                inline_keyboard_markup = {
                    'inline_keyboard':[
                        [
                            {'text':'Кнопа1','callback_data':'knopa1'},
                            {'text':'Кнопа2','callback_data':'knopa2'}
                        ],
                        [
                            {'text':'Кнопа3','callback_data':'knopa3'}
                        ]
                    ]
                }
                '''
                keyboard_button1 = {'text':'Кнопа1', 'callback_data':'knopa1'}
                keyboard_button2 = {'text':'Кнопа2', 'callback_data':'knopa2'}
                keyboard_button3 = {'text':'Кнопа3', 'callback_data':'knopa3'}
                keyboard_line1 = []
                keyboard_line2 = []
                keyboard_line1.append(keyboard_button1)
                keyboard_line1.append(keyboard_button2)
                keyboard_line2.append(keyboard_button3)
                keyboard_markup = []
                keyboard_markup.append(keyboard_line1)
                keyboard_markup.append(keyboard_line2)
                inline_keyboard_markup = {}
                inline_keyboard_markup.update({'inline_keyboard':keyboard_markup})

                tg.sendMessage(chat_id, "Кнопки, прикреплённые к сообщению.", reply_markup=inline_keyboard_markup)


            elif (text == "/sendPhoto"):

                keyboard_button = {'text':'Ссылка на фото', 'url':'http://f0430377.xsph.ru/test/logo.jpg'}
                keyboard_line = []
                keyboard_line.append(keyboard_button)
                keyboard_markup = []
                keyboard_markup.append(keyboard_line)
                inline_keyboard_markup = {}
                inline_keyboard_markup.update({'inline_keyboard':keyboard_markup})

                tg.sendPhoto(chat_id, "http://f0430377.xsph.ru/test/logo.jpg", "Место для описания фото.", reply_markup=inline_keyboard_markup)


            elif (text == "/sendAudio"):

                keyboard = [[{'text':'Ссылка на звук', 'url':'http://f0430377.xsph.ru/test/feil.mp3'}]]
                markup = {'inline_keyboard':keyboard}

                tg.sendAudio(chat_id, "http://f0430377.xsph.ru/test/feil.mp3", reply_markup=markup)


            elif (text == "/sendDocument"):

                tg.sendDocument(chat_id, "BQACAgIAAxkBAAIF8V9Lx6HhcT8lQSHLIupsB6Dkuq6xAAI0BgACUjRgSr_rlzM-LZIgGwQ", reply_markup=markup)


            elif (text == "/sendVideo"):

                tg.sendVideo(chat_id, "BAACAgIAAxkBAAIGBl9LzC3mUpoG825Ojn1_C18VZxdyAAI8BgACUjRgSt60Ojt9_vE_GwQ", reply_markup=markup)


            elif (text == "/sendAnimation"):

                tg.sendAnimation(chat_id, "CAACAgIAAxkBAAIGQF9L1eYgXiDE7fdAMNbF4DPGKavhAAIaAAP3AsgPry8JaXKONssbBA", reply_markup=markup)


            elif (text == "/sendVoice"):

                keyboard = [[{'text':'Ссылка на звук', 'url':'http://f0430377.xsph.ru/test/Golos.ogg'}]]
                markup = {'inline_keyboard':keyboard}

                tg.sendVoice(chat_id, "http://f0430377.xsph.ru/test/Golos.ogg", reply_markup=markup)


            elif (text == "/sendVideoNote"):

                tg.sendVideoNote(chat_id, "DQACAgIAAxkBAAIGlV9Mak9_ncBeg09fqHfWF20KhgGmAALEBgACUjRgShoykT2AQuj_GwQ", reply_markup=markup)


            elif (text == "/sendMediaGroup"):

                inputMedia = [{'type':'photo', 'media':'AgACAgIAAxkBAAIGqV9McYDHPPhFOUJs7q3nrUmaIOARAALBrTEbUjRgSjcmazkxR4UJ_ZZJli4AAwEAAwIAA3gAA1luAQABGwQ'},{'type':'photo', 'media':'http://f0430377.xsph.ru/test/logo.jpg', 'caption':'кэпшин *пуст*', 'parse_mode':'markdown'}]
                inputMediaPhoto = json.dumps(inputMedia)

                tg.sendMediaGroup(chat_id, inputMediaPhoto)


            elif (text == "/sendLocation"):

                tg.sendLocation(chat_id, 48.18585, 40.77424)


            elif (text == "/editMessageLiveLocation"):

                response = tg.sendLocation(chat_id, 48.18585, 40.77424, 60)
                tg.sendLocation(chat_id, 48.18585, 40.77424)

                tg.editMessageLiveLocation(chat_id, response['message_id'], 47.949728, 40.989386)
                tg.sendMessage(chat_id, "Первая локация после публикации изменена.")


            elif (text == "/stopMessageLiveLocation"):

                response = tg.sendLocation(chat_id, 48.18585, 40.77424, 60)
                tg.editMessageLiveLocation(chat_id, response['message_id'], 47.949728, 40.989386)
                tg.sendMessage(chat_id, "Включён запрет на изменение локации.")

                tg.stopMessageLiveLocation(chat_id, response['message_id'])


            elif (text == "/sendVenue"):

                tg.sendVenue(chat_id, 48.18585, 40.77424, "Заголовок", "Адрес")


            elif (text == "/sendContact"):

                tg.sendContact(chat_id, "+7 999 777 88", "Имя")


            elif (text == "/sendPoll"):

                tg.sendPoll(chat_id, "Вопрос", json.dumps(["Ответ1","Ответ2","Ответ3"]))


            elif (text == "/sendDice"):

                tg.sendDice(chat_id)


            elif (text == "/sendChatAction"):

                tg.sendMessage(chat_id, "В заголовке, под именем бота должна появиться надпись 'печатает...'")

                # Type of action to broadcast. Choose one, depending on what
                # the user is about to receive:

                # typing - for text messages,
                # upload_photo - for photos,
                # record_video or upload_video - for videos,
                # record_audio or upload_audio - for audio files,
                # upload_document - for general files,
                # find_location - for location data,
                # record_video_note or upload_video_note - for video notes.
                response = tg.sendChatAction(chat_id, "find_location")


            elif (text == "/getUserProfilePhotos"):

                response = tg.getUserProfilePhotos(from_id)
                tg.sendPhoto(chat_id, response['photos'][0][2]['file_id'])


            elif (text == "/getFile"):

                tg.sendPhoto(chat_id, "AgACAgIAAxkBAAIGqV9McYDHPPhFOUJs7q3nrUmaIOARAALBrTEbUjRgSjcmazkxR4UJ_ZZJli4AAwEAAwIAA3gAA1luAQABGwQ")

                # возвращает объект типа File
                # ссылка для скачивания файла - https://api.telegram.org/file/bot<token>/<file_path>
                response = tg.getFile("AgACAgIAAxkBAAIGqV9McYDHPPhFOUJs7q3nrUmaIOARAALBrTEbUjRgSjcmazkxR4UJ_ZZJli4AAwEAAwIAA3gAA1luAQABGwQ")

                tg.sendMessage(chat_id, "https://api.telegram.org/file/bot{0}/{1}".format(tg.token, response['file_path']))


            elif (text == "/kickChatMember"):

                tg.sendMessage(chat_id, "Перейди по ссылке в группу бота\n\nhttps://t.me/joinchat/Pezt-Buw0NqhYOXVVBbUxA")


            elif chat_id == groupHutor and new_chat_members_from_is_bot != True and new_chat_members != []: # method kickChatMember

                tg.sendMessage(chat_id, "Новый пользователь "+ new_chat_members[0].getFirstName() +" удалён из группы.")
                tg.kickChatMember(chat_id, new_chat_members[0].getId())


            elif (text == "/unbanChatMember"):

                tg.sendMessage(chat_id, "Перейди по ссылке:\n\nhttps://t.me/hutorTest2")


            elif chat_id == groupHutor2 and new_chat_members_from_is_bot != True and new_chat_members != []: # method unbanChatMember

                tg.sendMessage(chat_id, "Новый пользователь "+ new_chat_members[0].getFirstName() +" удалён из группы.")
                tg.sendMessage(chat_id, "C пользователя "+ new_chat_members[0].getFirstName() +" БАН снят.")

                tg.kickChatMember(chat_id, new_chat_members[0].getId())

                tg.unbanChatMember(chat_id, new_chat_members[0].getId())


            elif (text == "/restrictChatMember"):

                tg.sendMessage(chat_id, "Перейди по ссылке:\n\nhttps://t.me/hutorTest3")


            elif chat_id == groupHutor3 and new_chat_members_from_is_bot != True and new_chat_members != []: # method restrictChatMember

                tg.sendMessage(chat_id, "Welcome!")

                permissions = ChatPermissions()
                #permissions = ChatPermissions(None, True, True, True, True, True, True, True, True)
                #permissions.set(False,False,False,False,False,False,True,False)
                permissions.set(can_invite_users=True)

                tg.restrictChatMember(chat_id, new_chat_members[0].getId(), permissions.get())
                tg.sendMessage(chat_id, "Для нового пользователя установлены разрешения: всё запрещено, кроме приглашения новых участников.")


            elif text == "/getChat":
                tg.sendMessage(chat_id, "Просто")
                response = tg.getChat(groupHutor3)
                tg.sendMessage(chat_id, str(response.get()))


            elif text == "":
                return HttpResponse("ok")


            else:
                if (chat_type == "private"):
                    tg.sendMessage(chat_id, "чего?")

        # приём гет запроса
        elif request.GET["start"] == "1":
            return HttpResponse("Да, start равно 1")

    except Exception:
        return HttpResponse("ok")

    return HttpResponse("ok")



def givMeArray(val):
    array = []
    arr = []
    i = 0
    j = 0
    while i < len(val):
        while j < len(val[i]):
            arr.append(val[i][j])
            j += 1
        array.append(arr)
        j = 0
        i += 1
        arr = []
    return array


'''
# метод getMe с помощью функции call
result = tg.call("getMe")
first_name = result['first_name']
tg.call("sendMessage", "?chat_id=" + str(master) + "&text=" + str(first_name))
'''

#return HttpResponse(response.text)


# отправка сообщения
#requests.get("https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=1038937592&text=" + str(first_name))

'''
# тест запроса типа GET
response = requests.get("http://f0430377.xsph.ru/test/test.php")
#return HttpResponse(response.json())
return HttpResponse(response.text)
'''

# переадресация
#return HttpResponseRedirect("https://prizmarket.ru")

