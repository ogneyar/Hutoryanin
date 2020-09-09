#!/usr/bin/python3

from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
import json
import os

# для парсинга
from bs4 import BeautifulSoup

import http.cookies

import bmemcached


def test(request):

    response = header()

    response.write("<p>Это тестовый режим. (addons Heroku Memcash)</p>")

    servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
    user = os.environ.get('MEMCACHIER_USERNAME', '')
    passw = os.environ.get('MEMCACHIER_PASSWORD', '')

    mc = bmemcached.Client(servers, username=user, password=passw)

    mc.enable_retry_delay(True)  # Enabled by default. Sets retry delay to 5s.


    if mc.get("foo") is None:

        mc.set("foo", "bar")

    else:

        response.write( mc.get("foo") )


    #response.write("<p>Это тестовый режим. (request.META)</p>")
    #response.write( request.META )

    return response


def getCookie(request):

    ''' Сохранение куки методом HttpResponse().set_cookie
    '''
    response = header()

    response.write("<p>Это тестовый режим. (Сохранение куки HttpResponse().set_cookie('cooka', 'real', max_age=60))</p>")

    cookie = request.COOKIES

    if 'cooka' in cookie:
        response.write("<p>Куки установлена, её значение: '" + cookie['cooka'] + "'</p>")
    else:
        # установка куки
        response.set_cookie("cooka", "real", max_age=60)
        response.write("<p>Установил куки 'cooka'. Жми F5 чтобы удостовериться.</p>")

    return response



    ''' передача куки методом requests.get(url, cookies=cookies)
    '''
    response = HttpResponse()
    url = "http://"+request.META['HTTP_HOST']+"/test/cookie/"
    cookies = {'cooka':'real'}
    req = requests.get(url, cookies=cookies)

    response.write( str(req.text) )
    return response
    # а приём с помощью request.COOKIES



    ''' передача куки c помощью сессии
    '''
    response = HttpResponse()
    url = "http://"+request.META['HTTP_HOST']+"/test/cookie/"
    ssn = requests.Session()
    ssn.cookies.update({'cooka2':'too good real'})
    req = ssn.get(url)

    response.write( str(req.text) )
    return response


    ''' НЕ РАБОТАЕТ установка куки при помощи RequestsCookieJar

    jar = requests.cookies.RequestsCookieJar()
    jar.set('first_cookie', 'first', domain='127.0.0.1:8000', path='/cookies')
    jar.set('second_cookie', 'second', domain='127.0.0.1:8000', path='/extra')
    jar.set('third_cookie', 'third', domain='127.0.0.1:8000', path='/cookies')

    url = "http://127.0.0.1:8000/test/cookie/"
    req = requests.get(url, cookies=jar)

    return HttpResponse( str(req.text) )
    # returns '{ "cookies": { "first_cookie": "first", "third_cookie": "third" }}'

    '''


def cookie(request):

    response = header()

    # вывод информации об имеющихся куки
    response.write( json.dumps(request.COOKIES) )

    return response



def session(request):

    response = header()

    ''' сохранение сессии на 60 секунд
    '''
    if "session" in request.session:
        response.write( "Значение сессии 'session': " + str(request.session["session"]) )
    else:
        request.session.set_expiry(60)
        request.session["session"] = "too reel"
        response.write( "Сохранил сессию: {'session': 'too reel'}" )

    return response




def parser(request):

    response = header()

    ''' работающая версия парсинга сайта
    '''
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106",
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20200529.02.01'
    }

    #url = "https://www.youtube.com/watch?v=dGRJU_QlMf4&feature=youtu.be"

    url = "https://www.prizmarket.ru"

    page = requests.get(url, headers=headers)

    #soup = BeautifulSoup(page.text, "html.parser")
    soup = BeautifulSoup(page.text, "lxml")

    response.write( str(page.status_code)+"<br><br>"+str(soup.body.get_text()) )

    return response



# функция вывода заголовка на экран тестовых страниц
def header():

    response = HttpResponse()

    # вывод на экран
    response.write("<h1>Добро пожаловать!</h1>")

    response.write("<a href='/test/getcookie'>getCokie</a>  |  ")
    response.write("<a href='/test/cookie'>cokie</a>  |  ")
    response.write("<a href='/test/session'>session</a>  |  ")
    response.write("<a href='/test/parser'>parser</a>  |  ")
    response.write("<a href='/test'>назад</a>  |  <br><br>")

    return response



    ''' понял как передавать GET параметры

    query = {'q': 'Forest', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
    req = requests.get('https://pixabay.com/en/photos/', params=query)

    req.url
    # returns 'https://pixabay.com/en/photos/?order=popular&min_height=600&q=Forest&min_width=800'

    '''


