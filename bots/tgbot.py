from django.http import HttpResponse
from django.http import HttpResponseRedirect

import requests
import json
import os

from classes.tg.botApi import Bot
from classes.tg.types.replyKeyboardMarkup import ReplyKeyboardMarkup
from classes.tg.types.chatPermissions import ChatPermissions

# получение информации об апдейтах
global debug
debug = True
#debug = False

def bot(request):
    try:
        if (request.method == "POST"):

            token = os.getenv("TOKEN")
            master = int(os.getenv("MASTER"))

            groupHutor = -464572634 # group
            groupHutor2 = -1001471520704 # supergroup
            groupHutor3 = -1001393395949 # supergroup
            channelTestPodrobno = -1001444633822 # channel
            testerBotoff = 351009636

            # инициализация телеграм бота
            tg = Bot(token)

            if (debug):
                response = tg.sendMessage(master, request.body, disable_web_page_preview=True)
                #return HttpResponse("ok")

            update = None
            update = tg.start(request)

            if (debug):
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
            message_id = message.getMessageId()
            text = message.getText()
            #video_note = message.getVideoNote()

            message_from = message.getFrom()
            if message_from is not None:
                from_id = message_from.getId()
                from_first_name = message_from.getFirstName()
            else:
                from_id = 0
                from_first_name = "unknown"

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

            help_list2 += "------------\n\n"
            help_list2 += "/methods_one\n\n"

            keyboard = [[{'text':'Ссылка на PRIZMarket', 'url':'https://prizmarket.ru'}]]
            markup = {'inline_keyboard':keyboard}

            help = "Выбери один из списков методов Telegram API:\n\n/methods_one\n\n/methods_two"

            if (text == "/start"):
                if chat_id == master:
                    reply_keyboard_markup = {
                        'keyboard':[
                            [
                                {'text':'Публикация'},
                                {'text':'Скрыть'}
                            ]
                        ],
                        'resize_keyboard':True
                    }
                    response = tg.sendMessage(chat_id, "Здравствуй *Мастер*!\n\nЖми /help, если надо.", "markdown", reply_markup=reply_keyboard_markup)
                else:
                    response = tg.sendMessage(chat_id, "Здравствуй *" + from_first_name + "*!\n\nЖми /help", "markdown")


            elif (text == "Публикация" and chat_id == master):

                response = tg.sendMessage(chat_id, "Введи ссылку новой публикации.")


            elif (text == "/help"):

                response = tg.sendMessage(chat_id, help)


            elif (text == "/methods_one"):

                response = tg.sendMessage(chat_id, help_list)


            elif (text == "/methods_two"):

                response = tg.sendMessage(chat_id, help_list2)


            elif (text == "/sendMessage"):

                response = tg.sendMessage(chat_id, "Обычное сообщение.")


            elif (text == "/forwardMessage"):

                response = tg.forwardMessage(chat_id, chat_id, message_id)
                response = tg.sendMessage(chat_id, "Сообщение переслано.")


            elif (text == "/editMessageText"):

                response1 = tg.sendMessage(chat_id, "Смотри на этот текст")
                response2 = tg.sendMessage(chat_id, "Смотри на этот текст")
                response3 = tg.sendMessage(chat_id, "Смотри на этот текст")

                result = tg.editMessageText(chat_id, response1['message_id'], "Видишь?")
                response = tg.sendMessage(chat_id, "Сообщение изменено.")


            elif (text == "/deleteMessage"):

                response = tg.deleteMessage(chat_id, message_id)
                response = tg.sendMessage(chat_id, "Сообщение удалено.")


            elif (text == "тест"):

                yourArray = givMeArray([[1,2,3],[4,5,6],[7,8,9]])
                response = tg.sendMessage(chat_id, "Вот: " + str(yourArray))


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

                response = tg.sendMessage(chat_id, "Кнопки добавленны.", "markdown", True, None, 0, reply_keyboard_markup)


            elif (text == "/reply_keyboard_remove" or text == "Скрыть"):

                reply_keyboard_remove = {'remove_keyboard':True}
                response = tg.sendMessage(chat_id, "Кнопки удалены.", reply_markup=reply_keyboard_remove)


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

                response = tg.sendMessage(chat_id, "Кнопки, прикреплённые к сообщению.", reply_markup=inline_keyboard_markup)


            elif (text == "/sendPhoto"):

                keyboard_button = {'text':'Ссылка на фото', 'url':'http://f0430377.xsph.ru/test/logo.jpg'}
                keyboard_line = []
                keyboard_line.append(keyboard_button)
                keyboard_markup = []
                keyboard_markup.append(keyboard_line)
                inline_keyboard_markup = {}
                inline_keyboard_markup.update({'inline_keyboard':keyboard_markup})

                response = tg.sendPhoto(chat_id, "http://f0430377.xsph.ru/test/logo.jpg", "Место для описания фото.", reply_markup=inline_keyboard_markup)


            elif (text == "/sendAudio"):

                keyboard = [[{'text':'Ссылка на звук', 'url':'http://f0430377.xsph.ru/test/feil.mp3'}]]
                markup = {'inline_keyboard':keyboard}

                response = tg.sendAudio(chat_id, "http://f0430377.xsph.ru/test/feil.mp3", reply_markup=markup)


            elif (text == "/sendDocument"):

                response = tg.sendDocument(chat_id, "BQACAgIAAxkBAAIF8V9Lx6HhcT8lQSHLIupsB6Dkuq6xAAI0BgACUjRgSr_rlzM-LZIgGwQ", reply_markup=markup)


            elif (text == "/sendVideo"):

                response = tg.sendVideo(chat_id, "BAACAgIAAxkBAAIGBl9LzC3mUpoG825Ojn1_C18VZxdyAAI8BgACUjRgSt60Ojt9_vE_GwQ", reply_markup=markup)


            elif (text == "/sendAnimation"):

                response = tg.sendAnimation(chat_id, "CAACAgIAAxkBAAIGQF9L1eYgXiDE7fdAMNbF4DPGKavhAAIaAAP3AsgPry8JaXKONssbBA", reply_markup=markup)


            elif (text == "/sendVoice"):

                keyboard = [[{'text':'Ссылка на звук', 'url':'http://f0430377.xsph.ru/test/Golos.ogg'}]]
                markup = {'inline_keyboard':keyboard}

                response = tg.sendVoice(chat_id, "http://f0430377.xsph.ru/test/Golos.ogg", reply_markup=markup)


            elif (text == "/sendVideoNote"):

                response = tg.sendVideoNote(chat_id, "DQACAgIAAxkBAAIGlV9Mak9_ncBeg09fqHfWF20KhgGmAALEBgACUjRgShoykT2AQuj_GwQ", reply_markup=markup)


            elif (text == "/sendMediaGroup"):

                inputMedia = [{'type':'photo', 'media':'AgACAgIAAxkBAAIGqV9McYDHPPhFOUJs7q3nrUmaIOARAALBrTEbUjRgSjcmazkxR4UJ_ZZJli4AAwEAAwIAA3gAA1luAQABGwQ'},{'type':'photo', 'media':'http://f0430377.xsph.ru/test/logo.jpg', 'caption':'кэпшин *пуст*', 'parse_mode':'markdown'}]
                inputMediaPhoto = json.dumps(inputMedia)

                response = tg.sendMediaGroup(chat_id, inputMediaPhoto)


            elif (text == "/sendLocation"):

                response = tg.sendLocation(chat_id, 48.18585, 40.77424)


            elif (text == "/editMessageLiveLocation"):

                response = tg.sendLocation(chat_id, 48.18585, 40.77424, 60)
                response1 = tg.sendLocation(chat_id, 48.18585, 40.77424)

                response = tg.editMessageLiveLocation(chat_id, response['message_id'], 47.949728, 40.989386)
                response = tg.sendMessage(chat_id, "Первая локация после публикации изменена.")


            elif (text == "/stopMessageLiveLocation"):

                response = tg.sendLocation(chat_id, 48.18585, 40.77424, 60)
                response1 = tg.editMessageLiveLocation(chat_id, response['message_id'], 47.949728, 40.989386)
                response2 = tg.sendMessage(chat_id, "Включён запрет на изменение локации.")

                response = tg.stopMessageLiveLocation(chat_id, response['message_id'])


            elif (text == "/sendVenue"):

                response = tg.sendVenue(chat_id, 48.18585, 40.77424, "Заголовок", "Адрес")


            elif (text == "/sendContact"):

                response = tg.sendContact(chat_id, "+7 999 777 88", "Имя")


            elif (text == "ма"):

                response = tg.sendContact(chat_id, "+7 928 757 53 80", "Мама", reply_markup=markup)


            elif (text == "/sendPoll"):

                response = tg.sendPoll(chat_id, "Вопрос", json.dumps(["Ответ1","Ответ2","Ответ3"]))


            elif (text == "/sendDice"):

                response = tg.sendDice(chat_id)

                #response = tg.sendMessage(chat_id, "чего-то не работает...")
                #response = tg.sendDice(chat_id, "\ud83c\udfc0")



            elif (text == "/sendChatAction"):

                response = tg.sendMessage(chat_id, "В заголовке, под именем бота должна появиться надпись 'печатает...'")

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

                #response = tg.sendMessage(chat_id, "чего-то не работает...")

                response = tg.getUserProfilePhotos(from_id)

                response = tg.sendPhoto(chat_id, response['photos'][0][2]['file_id'])

                #response = tg.sendMessage(chat_id, "Возвращает объект UserProfilePhotos:\n\n" + json.dumps(response))


            elif (text == "/getFile"):

                response = tg.sendPhoto(chat_id, "AgACAgIAAxkBAAIGqV9McYDHPPhFOUJs7q3nrUmaIOARAALBrTEbUjRgSjcmazkxR4UJ_ZZJli4AAwEAAwIAA3gAA1luAQABGwQ")

                # возвращает объект типа File
                # ссылка для скачивания файла - https://api.telegram.org/file/bot<token>/<file_path>
                response = tg.getFile("AgACAgIAAxkBAAIGqV9McYDHPPhFOUJs7q3nrUmaIOARAALBrTEbUjRgSjcmazkxR4UJ_ZZJli4AAwEAAwIAA3gAA1luAQABGwQ")

                response = tg.sendMessage(chat_id, "https://api.telegram.org/file/bot{0}/{1}".format(tg.token, response['file_path']))


            elif (text == "/kickChatMember"):

                response = tg.sendMessage(chat_id, "Перейди по ссылке в группу бота\n\nhttps://t.me/joinchat/Pezt-Buw0NqhYOXVVBbUxA")


            elif chat_id == groupHutor and new_chat_members != []: # method kickChatMember

                response = tg.sendMessage(chat_id, "Новый пользователь "+ new_chat_members[0].getFirstName() +" удалён из группы.")
                response = tg.kickChatMember(chat_id, new_chat_members[0].getId())


            elif (text == "/unbanChatMember"):

                response = tg.sendMessage(chat_id, "Перейди по ссылке:\n\nhttps://t.me/hutorTest2")


            elif chat_id == groupHutor2 and new_chat_members != []: # method unbanChatMember

                response = tg.sendMessage(chat_id, "Новый пользователь "+ new_chat_members[0].getFirstName() +" удалён из группы.")
                response = tg.sendMessage(chat_id, "C пользователя "+ new_chat_members[0].getFirstName() +" БАН снят.")

                response = tg.kickChatMember(chat_id, new_chat_members[0].getId())

                response = tg.unbanChatMember(chat_id, new_chat_members[0].getId())


            elif (text == "/restrictChatMember"):

                response = tg.sendMessage(chat_id, "Перейди по ссылке:\n\nhttps://t.me/hutorTest3")


            elif chat_id == groupHutor3 and new_chat_members != []: # method restrictChatMember

                response = tg.sendMessage(chat_id, "Welcome!")

                permissions = ChatPermissions()

                #permissions = ChatPermissions(None, True, True, True, True, True, True, True, True)
                #permissions.set(False,False,False,False,False,False,True,False)
                permissions.set(can_invite_users=True)

                response = tg.restrictChatMember(chat_id, new_chat_members[0].getId(), permissions.get())
                response = tg.sendMessage(chat_id, "Для нового пользователя установлены разрешения: всё запрещено, кроме приглашения новых участников.")



            elif text == "/getChat":
                response = tg.sendMessage(chat_id, "Просто")
                response = tg.getChat(groupHutor3)
                response = tg.sendMessage(chat_id, str(response.get()))


            elif (text == "т"):

                #response = requests.get("https://youtu.be/dGRJU_QlMf4")
                response = requests.get("https://www.youtube.com/watch?v=dGRJU_QlMf4&feature=youtu.be")

                try:
                    response = tg.sendMessage(chat_id, "content \n\n" + str(response.content))
                except:
                    pass
                try:
                    response = tg.sendMessage(chat_id, "headers \n\n" + str(response.headers))
                except:
                    pass
                try:
                    response = tg.sendMessage(chat_id, "json \n\n" + str(response.json))
                except:
                    pass
                try:
                    response = tg.sendMessage(chat_id, "body \n\n" + str(response.body))
                except:
                    pass
                try:
                    response = tg.sendMessage(chat_id, "text \n\n" + str(response.text))
                except:
                    pass


            elif text == "э":
                db_url = os.getenv("DATABASE_URL")
                
                response = tg.sendMessage(chat_id, "db_url\n\n"+db_url)

                num = db_url.find("://")
                base = db_url[:num]
                db_url.replace(base+"://", "")
                
                response = tg.sendMessage(chat_id, "base\n\n"+base)
                
                num = db_url.find(":")
                user = db_url[:num]
                db_url.replace(user+":", "")
                
                response = tg.sendMessage(chat_id, "user\n\n"+user)
                
                num = db_url.find("@")
                passw = db_url[:num]
                db_url.replace(passw+"@", "")
                
                response = tg.sendMessage(chat_id, "passw\n\n"+passw)
                
                num = db_url.find(":")
                host = db_url[:num]
                db_url.replace(host+":", "")
                
                response = tg.sendMessage(chat_id, "host\n\n"+host)
                
                num = db_url.find("/")
                port = db_url[:num]
                db_url.replace(port+"/", "")
                
                response = tg.sendMessage(chat_id, "port\n\n"+port)
                
                name = db_url
                
                response = tg.sendMessage(chat_id, "name\n\n"+name)


            elif text == "":
                return HttpResponse("ok")


            else:
                if (chat_type == "private"):
                    response = tg.sendMessage(chat_id, "чего?")


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
    response = tg.call("sendMessage", "?chat_id=" + str(master) + "&text=" + str(first_name))
'''

    #return HttpResponse(response.text)


    # отправка сообщения
    #response = requests.get("https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=1038937592&text=" + str(first_name))

'''
    # тест запроса типа GET
    response = requests.get("http://f0430377.xsph.ru/test/test.php")
#    return HttpResponse(response.json())
    return HttpResponse(response.text)
'''

    # переадресация
    #return HttpResponseRedirect("https://prizmarket.ru")

    # приём гет запроса
'''
    try:
        if (request.GET["s"] == "t"):
            return HttpResponse('<br><br><br><br><br><center>O da!</center>')
        else:
            return HttpResponse('<br><br><br><br><br><center>Hello from Python!</center>')
    except Exception:
        return HttpResponse('<br><br><br><br><br><center>Hello with Exception!</center>')
'''
