#!/usr/bin/python3

from django.http import HttpResponse
from django.http import HttpResponseRedirect

import os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from classes.tg.botApi import Bot


def send(request):
    
    if request.POST:
        return HttpResponse("Post: "+str(request.POST))
    else:
        return HttpResponseRedirect("/")

    if request.get_host() == '127.0.0.1:8000':

        smtp_login = "hutor_yanin@sibnet.ru"
        smtp_pass = "***"
        smtp_port = 25
        smtp_server = "smtp.sibnet.ru"

        token = "***"
        master = 1038937592

    else:

        smtp_login = str(os.getenv("SMTP_LOGIN"))
        smtp_pass = str(os.getenv("SMTP_PASSWORD"))
        smtp_port = int(os.getenv("SMTP_PORT"))
        smtp_server = str(os.getenv("SMTP_SERVER"))

        token = os.getenv("TOKEN")
        master = int(os.getenv("MASTER"))

    response = HttpResponse()

    tg = Bot(token)
    
    
    if request.POST["email"] != "":
        if request.POST["message"] != "":
            r = tg.sendMessage(master, request.POST["email"] + "\n\n" +request.POST["message"])
            response.write("<br><br><br><center><h1>Письмо отправленно!</h1></center><br><br>")
            response.write("<center><a href='/'>Вернуться на главную страницу</a></center>")
        else:
            response.write("<br><br><br><center><h3>Необходимо описать суть вопроса!</h3></center><br><br>")
            response.write("<center><a href='/support'>Вернуться назад</a></center>")
    else:
        response.write("<br><br><br><center><h3>Необходимо указать Ваш email!</h3></center><br><br>")
        response.write("<center><a href='/support'>Вернуться назад</a></center>")


    return response



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


    '''
    import email_to

    server = email_to.EmailServer(smtp_server, smtp_port, smtp_login, smtp_pass)
    server.quick_email('ya13th@mail.ru', 'Test',
        ['# A Heading', 'Something else in the body'],
        style='h1 {color: blue}')
    '''




