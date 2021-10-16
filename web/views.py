from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Greeting, Url, Messages, Users
from .forms import UsersForm

import os, bmemcached, smtplib, random
#import requests, json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from classes.tg.botApi import Bot


discount = 10
discount_until = "31.12.2021"


def index(request):
    parameters = {
        'discount':discount,
        'discount_until':discount_until
    }
    return render(request, "index.html", parameters)


def temp(request):

    return render(request, "temp/temp.html")


def privacy(request):

    return render(request, "privacy.html")


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



def getRussianName(product):
    russianName = 'none'
    if product == 'high_knife_bee':
        russianName = 'Шмель'
    if product == 'middle_knife_bee':
        russianName = 'Пчела'
    if product == 'low_knife_bee':
        russianName = 'Жучёк'

    # if product == 'high_knife' or product == 'middle_knife' or product == 'low_knife':
    #     russianName = product

    if product == 'high_knife':
        russianName = 'Брат'
    if product == 'middle_knife':
        russianName = 'Друг'
    if product == 'low_knife':
        russianName = 'Товарищ'

    if product == 'high_spoon':
        russianName = 'Царица'
    if product == 'middle_spoon':
        russianName = 'Мера'
    if product == 'low_spoon':
        russianName = 'Кроха'
    
    if product == 'site':
        russianName = 'Сайт'
    if product == 'tgbot':
        russianName = 'Бота'
    if product == 'vkbot':
        russianName = 'Бота'
    if product == 'android':
        russianName = 'Приложение'
    
    return russianName

def creating_an_order(request, category, product):
    user = "none"
    if "user" in request.session:
        user = request.session["user"]

    russianName = getRussianName(product)

    color = ""
    
    if request.method == "GET":
        if 'color' in request.GET:
            #color = request.GET["color"]   
            if russianName == 'Шмель':
                color = getColorMen(request.GET["color"])
            if russianName == 'Пчела':
                color = getColor(request.GET["color"])    

    parameters = {
        'user':user,
        'category':category,
        'product':product,
        'russianName':russianName,
        'color':color
    }
    return render(request, "products/creating_an_order.html", parameters)




def knives(request):

    return render(request, "products/knives/knives.html")

def low_knife(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/knives/low_knife.html", data)

def middle_knife(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/knives/middle_knife.html", data)

def high_knife(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/knives/high_knife.html", data)



def getColor(color):
    colorInRussian = ''
    if color == 'blue':
        colorInRussian = 'Синяя'
    if color == 'red':
        colorInRussian = 'Красная'
    if color == 'green':
        colorInRussian = 'Зелёная'
    if color == 'transparent':
        colorInRussian = 'Прозрачная'
    if color == 'orange':
        colorInRussian = 'Оранжевая'
    return colorInRussian

def getColorMen(color):
    colorInRussianMen = ''
    if color == 'blue':
        colorInRussianMen = 'Синий'
    if color == 'red':
        colorInRussianMen = 'Красный'
    if color == 'green':
        colorInRussianMen = 'Зелёный'
    if color == 'transparent':
        colorInRussianMen = 'Прозрачный'
    if color == 'orange':
        colorInRussianMen = 'Оранжевый'
    return colorInRussianMen

def getParameters(request):
    color = ""
    colorInRussian = ""
    colorInRussianMen = ''

    if request.method == "GET":
        if 'color' in request.GET:
            color = request.GET["color"]
            colorInRussian = getColor(color)
            colorInRussianMen = getColorMen(color)
    
    parameters = {
        'color':color,
        'colorInRussian':colorInRussian,
        'colorInRussianMen':colorInRussianMen,
        "discount": discount,
        "discount_until": discount_until
    }
    return parameters


def low_knife_bee(request):
    parameters = getParameters(request)    
    return render(request, "products/knives/low_knife_bee.html", parameters)


def middle_knife_bee(request):
    parameters = getParameters(request)
    return render(request, "products/knives/middle_knife_bee.html", parameters)


def high_knife_bee(request):
    parameters = getParameters(request)
    return render(request, "products/knives/high_knife_bee.html", parameters)



def spoons(request):

    return render(request, "products/spoons/spoons.html")

def low_spoon(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/spoons/low_spoon.html", data)

def middle_spoon(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/spoons/middle_spoon.html", data)

def high_spoon(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/spoons/high_spoon.html", data)



def candlesticks(request):

    return render(request, "products/candlesticks/candlesticks.html")

def low_candlestick(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/candlesticks/low_candlestick.html", data)

def middle_candlestick(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/candlesticks/middle_candlestick.html", data)

def high_candlestick(request):

    data = {
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "products/candlesticks/high_candlestick.html", data)



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

    parameters = {
        'discount':discount,
        'discount_until':discount_until
    }

    return render(request, "promo/promo.html", parameters)


def promo_result(request):

    all_users = Users.objects.all()
    promo1 = []
    # promo2 = []
    i_promo1 = 0
    # i_promo2 = 0

    for user in all_users:
        if user.info != "none":
            promo1.append(user)
            i_promo1 = i_promo1 + 1
        # if user.info == "yes":
        #     promo2.append(user)
        #     i_promo2 = i_promo2 + 1
    
    if (i_promo1 > 2):
        promo1_win1 = random.randint(1,i_promo1)
        promo1_win2 = random.randint(1,i_promo1)
        promo1_win3 = random.randint(1,i_promo1)
        while (promo1_win1 == promo1_win2):
            promo1_win2 = random.randint(1,i_promo1)
        while ((promo1_win3 == promo1_win2)or(promo1_win3 == promo1_win1)):
            promo1_win3 = random.randint(1,i_promo1)
    elif (i_promo1 == 2):
        promo1_win1 = random.randint(1,i_promo1)
        if (promo1_win1 == 2):
            promo1_win2 = 1
        else:
            promo1_win2 = 2       
        promo1_win3 = 0
    elif (i_promo1 == 1):
        promo1_win1 = 1
        promo1_win2 = 0
        promo1_win3 = 0
    else:
        promo1_win1 = 0
        promo1_win2 = 0
        promo1_win3 = 0

    # if (i_promo2 > 1):
    #     promo2_win1 = random.randint(1,i_promo2)
    #     promo2_win2 = random.randint(1,i_promo2)
    #     while (promo2_win2 == promo2_win1):
    #         promo2_win2 = random.randint(1,i_promo2)
    # elif (i_promo2 == 1):
    #     promo2_win1 = 1
    #     promo2_win2 = 0
    # else:
    #     promo2_win1 = 0
    #     promo2_win2 = 0
    
    i = 1
    for pr1 in promo1:
        if (i == promo1_win1):
            promo1_win1 = pr1.login
        if (i == promo1_win2):
            promo1_win2 = pr1.login
        if (i == promo1_win3):
            promo1_win3 = pr1.login
        i = i + 1
    
    # i = 1
    # for pr2 in promo2:
    #     if (i == promo2_win1):
    #         promo2_win1 = pr2.login
    #     if (i == promo2_win2):
    #         promo2_win2 = pr2.login
    #     i = i + 1

    data = {
        "promo1": promo1,
        "promo1_win1": promo1_win1,
        "promo1_win2": promo1_win2,
        "promo1_win3": promo1_win3,
        # "promo2": promo2,
        # "promo2_win1": promo2_win1,
        # "promo2_win2": promo2_win2
    }

    return render(request, "promo/promo_result.html", data)


def promo_winner(request):

    promo1_win1 = ""
    promo1_win2 = ""
    promo1_win3 = ""

    promo2_win1 = ""
    promo2_win2 = ""
    if request.method == "POST":
        if "promo1_win1" in request.POST:
            promo1_win1 = request.POST["promo1_win1"]
        if "promo1_win2" in request.POST:
            promo1_win2 = request.POST["promo1_win2"]
        if "promo1_win3" in request.POST:
            promo1_win3 = request.POST["promo1_win3"]
        
        if "promo2_win1" in request.POST:
            promo2_win1 = request.POST["promo2_win1"]
        if "promo2_win2" in request.POST:
            promo2_win2 = request.POST["promo2_win2"]
    
    data = {
        "promo1_win1": promo1_win1,
        "promo1_win2": promo1_win2,
        "promo1_win3": promo1_win3,
        "promo2_win1": promo2_win1,
        "promo2_win2": promo2_win2
    }

    return render(request, "promo/promo_winner.html", data)
    



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

    user = "none"
    fail = "none"
    login = "none"

    if request.method == "POST":
        all_users = Users.objects.order_by('id')
        if "login" in request.POST:
            login = request.POST["login"]
            for usr in all_users:
                if usr.login == login:
                    if "password" in request.POST:
                        password = request.POST["password"]
                        if usr.password == password:
                            user = {
                                'login':usr.login,
                                'password':usr.password,
                                'promo':usr.promo,
                                'email':usr.email,
                                'adress':usr.adress
                            }
                            request.session["user"] = user

                        else:
                            fail = "Не верный пароль!"
            if user == "none":
                fail = "Не верный логин!"

    elif "user" in request.session:
        user = request.session["user"]

    data = {
        "user": user,
        "fail": fail,
        "login": login,
        "discount": discount,
        "discount_until": discount_until
    }

    return render(request, "lk/lk.html", data)


def exit(request):
    request.session["user"] = "none"

    return HttpResponseRedirect("/lk")


def registration(request):
    global tg, master

    token = os.getenv("TOKEN")
    master = int(os.getenv("MASTER"))
    admin_group = int(os.getenv("ADMIN_GROUP"))
    host = 'no_local'

    tg = Bot(token)

    mail = "none"
    fail = "none"
    login = "none"
    email = "none"
    #adress = "none"

    if request.method == "POST":
        all_users = Users.objects.order_by('id')

        login = request.POST["login"]
        password = getPass(10)
        email = request.POST["email"]
        #adress = request.POST["adress"]
        promo = getPass(5)

        if login == "":
            fail = "Необходимо ввести логин!"
        elif email == "":
            fail = "Необходимо ввести email!"
        #elif adress == "":
        #    fail = "Необходимо ввести адрес!"
        else:
            for usr in all_users:
                if usr.login == login:
                    fail = "Этот логин уже занят!"
                elif usr.email == email:
                    fail = "Этот email уже занят!"

            if fail == "none":
                new_record = {
                    'login':login,
                    'password':password,
                    'email':email,
                    'adress':'none',
                    'promo':promo,
                    'info':'none'
                }
                form = UsersForm(new_record)
                if form.is_valid():
                    sms = "Регистрация!\n\nВаш логин: "+login+"\n\nВаш пароль: "+password+"\n\n\nhttp://"+request.get_host()+"/lk"
                    mail = sendMailTo(email, "Регистрация на сайте ХуторянинЪ.", sms)
                    if mail != "Ошибка отправки!":
                        form.save()
                        tg.sendMessage(admin_group, "Зарегистрировал нового клиента:\n\n" + login + "\n\n" + email)
                else:
                    mail = "Ошибка формы!"

    data = {
        "mail": mail,
        "fail": fail,
        "login": login,
        #"adress": adress,
        "email": email
    }

    return render(request, "lk/registration.html", data)


def forget_password(request):
    all_users = Users.objects.order_by('id')

    mail = "none"
    fail = "none"
    forget_password = "none"
    #forget = "none"
    login = "none"
    old_password = "none"
    new_password = "none"
    new_password2 = "none"    

    if request.method == "POST":
        # если клиент ввёл новый пароль
        if 'forget' in request.POST:
            #forget = request.POST["forget"]

            if 'login' in request.POST:
                login = request.POST["login"]
            if 'old_password' in request.POST:
                old_password = request.POST["old_password"]
            if 'new_password' in request.POST:
                new_password = request.POST["new_password"]
            if 'new_password2' in request.POST:
                new_password2 = request.POST["new_password2"]

            if new_password == new_password2:
                for usr in all_users:
                    if usr.login == login:
                        if usr.password == old_password:
                            new_record = {
                                'login':login,
                                'password':new_password,
                                'email':usr.email,
                                'adress':usr.adress,
                                'promo':usr.promo,
                                'info':usr.info
                            }
                            article = Users.objects.get(id=usr.id)
                            form = UsersForm(new_record, instance=article)
                            if form.is_valid():
                                form.save()
                            mail = "Ваш пароль обновлён!"
            else:
                fail = "Ошибка повтора пароля!"
                forget_password = "yes"


        elif 'email' in request.POST:
            # если клиент нажал "забыли пароль?"
            email = request.POST["email"]

            if email == "":
                fail = "Введите email!"
            else:
                for usr in all_users:
                    if usr.email == email:
                        login = usr.login
                        old_password = usr.password

                if login == "none":
                    fail = "В базе нет такого email!"
                else:
                    mail = sendMailTo(email, "Сброс пароля на сайте ХуторянинЪ.", "Ссылка для сброса пароля\n\nhttp://"+request.get_host()+"/forget_password?login="+login+"&old_password="+old_password)

    elif request.method == "GET":
        # если клиент пришёл по ссылке для восстановления пароля
        if 'login' in request.GET and 'old_password' in request.GET:
            login = request.GET["login"]
            old_password = request.GET["old_password"]

            for usr in all_users:
                if usr.login == login:
                    if usr.password == old_password:
                        forget_password = "yes"

    data = {
        "mail": mail,
        "fail": fail,
        "forget_password": forget_password,
        "login": login,
        "new_password": new_password,
        "old_password": old_password
    }

    return render(request, "lk/forget_password.html", data)



def about(request):

    return render(request, "about.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



# функция отправки Email
def sendMailTo(to_whom, subject, body):
    #global smtp_login, smtp_pass, smtp_port, smtp_server

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


def getPass(n):

    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    password =''
    for i in range(n):
        password += random.choice(chars)

    return password
