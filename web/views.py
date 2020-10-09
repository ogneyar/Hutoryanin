from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Greeting, Url, Messages, Users
from .forms import UsersForm

import os, bmemcached, smtplib, random
#import requests, json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from classes.tg.botApi import Bot


def index(request):

    return render(request, "index.html")


def public(request):

    all_url = Url.objects.order_by('-id')
    length = len(all_url)
    remains = length % 9
    if remains == 0:
        quantity = length / 9
    else:
        length = length - remains
        quantity = length / 9 + 1

    parameters = {
        'all_url':all_url,
        'quan_page':range(int(quantity)+1),
        'page_id':0
    }

    return render(request, "public.html", parameters)


def public_page(request, page_id):

    page_id = int(page_id)
    all_url = Url.objects.order_by('-id')
    length = len(all_url)
    remains = length % 9
    if remains == 0:
        quantity = length / 9
    else:
        length = length - remains
        quantity = length / 9 + 1

    if page_id > quantity or page_id < 0:
        raise Http404("Нет такой страницы!")

    if page_id == quantity:
        all_url = all_url[(((page_id-1)*9)+1):]
    else:
        all_url = all_url[((page_id-1)*9):(page_id*9)]

    parameters = {
        'all_url':all_url,
        'quan_page':range(int(quantity)+1),
        'page_id':page_id
    }

    return render(request, "public.html", parameters)



def products(request):

    return render(request, "products/products.html")

def creating_an_order(request, category, product):

    return render(request, "products/creating_an_order.html", {'category':category,'product':product})

def knives(request):

    return render(request, "products/knives/knives.html")

def low_knife(request):

    return render(request, "products/knives/low_knife.html")

def middle_knife(request):

    return render(request, "products/knives/middle_knife.html")

def high_knife(request):

    return render(request, "products/knives/high_knife.html")

def spoons(request):

    return render(request, "products/spoons/spoons.html")

def low_spoon(request):

    return render(request, "products/spoons/low_spoon.html")

def middle_spoon(request):

    return render(request, "products/spoons/middle_spoon.html")

def high_spoon(request):

    return render(request, "products/spoons/high_spoon.html")

def candlesticks(request):

    return render(request, "products/candlesticks/candlesticks.html")

def low_candlestick(request):

    return render(request, "products/candlesticks/low_candlestick.html")

def middle_candlestick(request):

    return render(request, "products/candlesticks/middle_candlestick.html")

def high_candlestick(request):

    return render(request, "products/candlesticks/high_candlestick.html")


def applications(request):

    return render(request, "products/applications/applications.html")

def site(request):

    return render(request, "products/applications/site.html")

def tgbot(request):

    return render(request, "products/applications/tgbot.html")

def vkbot(request):

    return render(request, "products/applications/vkbot.html")

def android(request):

    return render(request, "products/applications/android.html")



def promo(request):

    return render(request, "promo.html")



def support(request):

    if request.get_host() != '127.0.0.1:8000':

        mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
        mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
        mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')

        mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
        mc.enable_retry_delay(True)

        if mc.get("repeat") is not None:
            mc.delete("repeat")
    else:

        if "repeat" in request.session:

           del request.session["repeat"]

    return render(request, "support/support.html")


def lk(request):

    if request.method == "POST":
        all_users = Users.objects.order_by('id')
        for user in all_users:
            if user.login == request.POST["login"]:
                if user.password == request.POST["password"]:
                    request.session["user"] = request.POST["login"]


    ''' сохранение сессии
    '''
    if "user" in request.session:
        user = str(request.session["user"])
    else:
        user = 'none'
        #request.session.set_expiry(60)
        #request.session["user"] = "Огнеяр"

    return render(request, "lk/lk.html", {"user": user})


def exit(request):
    request.session["user"] = "none"

    return HttpResponseRedirect("/lk")


def registration(request):
    global tg, master

    if request.get_host() == '127.0.0.1:8000':
        token = "1224906863:AAHYalxznzb4XwcP-7olgPu8BQjNJ0LrKXY"
        master = 1038937592
        host = 'local'
    else:
        token = os.getenv("TOKEN")
        master = int(os.getenv("MASTER"))
        host = 'no_local'

    tg = Bot(token)

    mail = 'none'

    if request.method == "POST":
        login = request.POST["login"]
        password = getPass()
        email = request.POST["email"]
        data = {
            'login':login,
            'password':password,
            'email':email,
            'adress':request.POST["adress"],
            'promo':'Новичёк',
            'info':'none'
        }
        form = UsersForm(data)
        if form.is_valid():
            sms = "Ваш логин: "+login+"\n\nВаш пароль: "+password+"\n\n\nhttp://"+request.get_host()+"/lk"
            mail = sendMailTo(host, email, "Регистрация на сайте ХуторянинЪ.", sms)
            if mail != "Ошибка отправки!":
                form.save()
                tg.sendMessage(master, "Зарегистрировал нового клиента:\n\n" + login + "\n\n" + email)

    return render(request, "lk/registration.html", {"mail": mail})


def forget_password(request):
    if request.get_host() == '127.0.0.1:8000':
        host = 'local'
    else:
        host = 'no_local'

    if request.method == "POST":
        email = request.POST["email"]
        mail = sendMailTo(host, email, "Сброс пароля на сайте ХуторянинЪ.", "Здесь будет ссылка для сброса пароля")
    else:
        mail = 'none'

    return render(request, "lk/forget_password.html", {"mail": mail})



def about(request):

    return render(request, "about.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



# функция отправки Email
def sendMailTo(host, to_whom, subject, body):
    #global smtp_login, smtp_pass, smtp_port, smtp_server

    if host == 'local':
        '''
        smtp_login = "hutoryanin_test@mail.ru"
        smtp_pass = "Polkmn_111"
        '''
        smtp_login = "prizmarket@mail.ru"
        smtp_pass = "Qwrtui13"

        smtp_port = 465
        smtp_server = "smtp.mail.ru"
    else:
        smtp_login = str(os.getenv("SMTP_LOGIN"))
        smtp_pass = str(os.getenv("SMTP_PASSWORD"))
        smtp_port = int(os.getenv("SMTP_PORT"))
        smtp_server = str(os.getenv("SMTP_SERVER"))

    try:
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = smtp_login
        message.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_login, smtp_pass)
        server.sendmail(smtp_login, to_whom, message.as_string())
        server.quit()

        return "Письмо отправленно, проверьте почту! Если не пришло письмо, загляните в папку спам."
    except:
        return "Ошибка отправки!"


def getPass():

    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    password =''
    for i in range(10):
        password += random.choice(chars)

    return password
