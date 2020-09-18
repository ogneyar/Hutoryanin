#!/usr/bin/python3

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

import os, smtplib, requests, json, bmemcached

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from classes.tg.botApi import Bot


mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')

mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
mc.enable_retry_delay(True)


def send(request):

    if request.method != "POST" or "email" not in request.POST or "message" not in request.POST:
            return HttpResponseRedirect("/")

    if request.get_host() == '127.0.0.1:8000':

        '''
        smtp_login = "hutor_yanin@sibnet.ru"
        smtp_pass = ""
        smtp_port = 25
        smtp_server = "smtp.sibnet.ru"
        '''

        smtp_login = "prizmarket@mail.ru"
        smtp_pass = ""
        smtp_port = 465
        smtp_server = "smtp.mail.ru"

        token = ""
        master = 1038937592

    else:

        smtp_login = str(os.getenv("SMTP_LOGIN"))
        smtp_pass = str(os.getenv("SMTP_PASSWORD"))
        smtp_port = int(os.getenv("SMTP_PORT"))
        smtp_server = str(os.getenv("SMTP_SERVER"))

        token = os.getenv("TOKEN")
        master = int(os.getenv("MASTER"))


    #resp = HttpResponse()

    response = ""

    tg = Bot(token)

    if request.POST["email"] != "":
        if request.POST["message"] != "":

            if request.get_host() != '127.0.0.1:8000':

                if mc.get("repeat") is None:

                    mc.set("repeat", "yes")

                    r = tg.sendMessage(master, request.POST["email"] + "\n\n" +request.POST["message"])

                    response += "Письмо отправленно!"

                else:

                    response += "Письмо уже отправленно!"

            else:

                try:
                    # сохранение сессии
                    if "repeat" not in request.session:
                        # удаление через 60 секунд
                        #request.session.set_expiry(60)
                        request.session["repeat"] = "yes"

                        r = tg.sendMessage(master, request.POST["email"] + "\n\n" +request.POST["message"])

                        response += "Письмо отправленно!"

                    else:

                        response += "Письмо уже отправленно!"

                except:

                    response += "Exception: SESSION_ENGINE необходимо закоментировать в settings.py"


            ''' отправка письма

            import email_to

            server = email_to.EmailServer(smtp_server, smtp_port, smtp_login, smtp_pass)

            message = server.message()
            message.add('# Oh boy, something went wrong!')
            message.add('- The server had a hiccup')
            message.add('- The power went out')
            message.add('- Blame it on a rogue backhoe')
            message.style = 'h1 { color: red}'

            message.send('ya13th@mail.ru', 'Things did not occur as expected')

            #server.quick_email('ya13th@mail.ru', 'Test',
            #    ['# A Heading', 'Something else in the body'],
            #    style='h1 {color: blue}')
            '''


        else:
            response += "Необходимо описать суть вопроса или предложения!"

    else:
        response += "Необходимо указать Ваш email!"



    return render(request, "sendmail.html", {'response':response})



    #return HttpResponse("Отправил")


    '''
    message = MIMEMultipart()

    message['Subject'] = 'Test'
    message['From'] = 'user@gmail.com'
    message['To'] = 'someone@else.com'


    message.attach(MIMEText('# A Heading\nSomething else in the body', 'plain'))
    #message.attach(MIMEText('<h1 style="color: blue">A Heading</a><p>Something else in the body</p>', 'html'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_login, smtp_pass)
    server.sendmail(smtp_login, 'ya13th@mail.ru', message.as_string())
    server.quit()
    '''







