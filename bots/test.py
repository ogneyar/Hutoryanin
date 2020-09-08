#!/usr/bin/python3

from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
import json
import os

# для парсинга
from bs4 import BeautifulSoup

# робота с куки и сессиями
from django.shortcuts import redirect


import http.cookies


def start(request):

    url = "http://127.0.0.1:8000/test/cookies/"

    r = requests.get(url)


    #if "cookie" in r.cookies:
    if r.cookies.get('cook') is not None:

        return HttpResponse( r.cookies.get('cook') )

    else:
        '''
        cookies = {'cook':'real'}

        r = requests.get(url, cookies=cookies)

        return HttpResponse( "Установил cookie." + str(r.cookies.get('cook')) )
        '''


        ''' установка куки

        jar = requests.cookies.RequestsCookieJar()
        jar.set('first_cookie', 'first', domain='httpbin.org', path='/cookies')
        jar.set('second_cookie', 'second', domain='httpbin.org', path='/extra')
        jar.set('third_cookie', 'third', domain='httpbin.org', path='/cookies')

        url = 'http://httpbin.org/cookies'
        req = requests.get(url, cookies=jar)

        return HttpResponse( "Установил cookie." + str(req.text) )

        # returns '{ "cookies": { "first_cookie": "first", "third_cookie": "third" }}'

        '''


        ssn = requests.Session()
        ssn.cookies.update({'visit-month': 'February'})

        #url = 'http://httpbin.org/cookies'
        reqOne = ssn.get(url)
        return HttpResponse( "Установил cookie." + str(reqOne.text) )


def cookie(request):

    return HttpResponse( "Куки" )


def session(request):

    ''' сохранение сессии на 60 секунд
    '''

    if "session" in request.session:

        return HttpResponse( "Значение сессии 'session': " + str(request.session["session"]) )

    else:

        request.session.set_expiry(60)
        request.session["session"] = "too reel"


        return HttpResponse( "Сохранил сессию: {'session': 'tooreel'}" )




    ''' понял как передавать GET параметры

    query = {'q': 'Forest', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
    req = requests.get('https://pixabay.com/en/photos/', params=query)

    req.url
    # returns 'https://pixabay.com/en/photos/?order=popular&min_height=600&q=Forest&min_width=800'

    '''



    ''' работающая версия парсинга сайта

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

    return HttpResponse( str(page.status_code)+"<br><br>"+str(soup.body.get_text()) )

    '''



