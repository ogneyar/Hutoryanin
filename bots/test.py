from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests, json, os, bmemcached
from bs4 import BeautifulSoup


mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')
mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
mc.enable_retry_delay(True)  # Enabled by default. Sets retry delay to 5s.


# функция вывода заголовка на экран тестовых страниц
def header():

    response = HttpResponse()

    # вывод на экран  h1{text-align:center;}  justify-content:center;
    response.write("<style type='text/css'>*{-webkit-hyphens:auto;-moz-hyphens:auto;-ms-hyphens:auto;hyphens:auto;word-wrap:break-word;}a{text-decoration:none;border:1px solid #8c8c8c;border-radius:5px; margin:5px; padding: 5px 10px;}div{display: flex;flex-wrap: wrap;}</style>")

    response.write("<meta name='viewport' content='user-scalable=yes, width=device-width, initial-scale=1.0, maximum-scale=1.0'>")

    response.write("<h1>Добро пожаловать!</h1>")

    #response.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    response.write("<div><a href='/test/prizm'>TESTMarket</a>")
    response.write("<a href='/test/7yanika'>TEST7yanika</a>")
    response.write("<a href='/test/hutor'>TESThutor</a>")
    response.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    response.write("<a href='https://sph.hutoryanin.online'>Sprint</a>")
    response.write("<a href='https://heroku.hutoryanin.online'>Heroku</a>")
    response.write("<a href='https://beget.hutoryanin.online'>Beget</a></div><br>")


    #response.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    response.write("<div><a href='/test/vanilla'>vanilla</a>")
    response.write("<a href='/test/fullPageScrolling'>fullPageScrolling</a>")
    response.write("<a href='/test/neonButton'>neonButton</a>")
    response.write("<a href='/test/sidebarMenu'>sidebarMenu</a>")
    response.write("<a href='/test/cardHoverEffects'>cardHoverEffects</a>")
    response.write("<a href='/test/parallaxScrollingEffect'>parallaxScrollingEffect</a></div><br>")


    #response.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    response.write("<div><a href='/test/getcookie'>getCokie</a>")
    response.write("<a href='/test/cookie'>cokie</a>")
    response.write("<a href='/test/session'>session</a>")
    response.write("<a href='/test/parser'>parser</a>")
    response.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    response.write("<a href='/test/testjs'>testjs</a>")
    response.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    response.write("<a href='/test'>Назад</a></div><br><br>")

    return response


def test(request):

    response = header()

    try:

        if request.get_host() == '127.0.0.1:8000':

            response.write("<p>Это тестовый режим. (addons Heroku Memcash, но на локальной машине используется куки.)</p>")

            cookie = request.COOKIES

            if 'foo' in cookie:
                response.write( "<p>Записана кука 'foo': "  + cookie['foo'] + '</p>' )

            else:
                response.set_cookie("foo", "bar", max_age=60)
                response.write( '<p>Записал куки {"foo":"bar"}</p>' )

        else:

            response.write("<p>Это тестовый режим. (addons Heroku Memcash)</p>")

            if mc.get("foo") is None:

                mc.set("foo", "bar")
                response.write( '<p>Записал {"foo":"bar"}</p>' )

            else:

                response.write( "<p>Записана в мемкеш 'foo': " + mc.get("foo") + '</p>' )

                mc.delete("foo")
                response.write( "<p>И сразу удалил foo.</p>" )

                mc.delete("this")
                response.write( "<p>Пробую удалить несуществующую запись в memcached</p>" )



        response.write("<br><br><p>Это тестовый режим. (request.META)</p>")
        response.write( request.META )


    except:

        response.write("<p>Exception</p>")

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




    ''' передача куки методом requests.get(url, cookies=cookies) Не работает(
    '''
    response = HttpResponse()
    url = "http://"+request.META['HTTP_HOST']+"/test/cookie/"
    cookies = {'cooka':'real'}
    req = requests.get(url, cookies=cookies)

    response.write( str(req.text) )
    response.write( "<br><br>" )
    response.write( json.dumps(request.COOKIES) )
    return response
    # а приём с помощью request.COOKIES




    ''' передача куки c помощью сессии Не работает(
    '''
    response = HttpResponse()
    url = "http://"+request.META['HTTP_HOST']+"/test/cookie/"
    ssn = requests.Session()
    ssn.cookies.update({'cooka2':'too good real'})
    req = ssn.get(url)

    response.write( str(req.text) )
    response.write( "<br><br>" )
    response.write( json.dumps(request.COOKIES) )
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

    try:

        ''' сохранение сессии на 60 секунд
        '''
        if "session" in request.session:
            response.write( "Значение сессии 'session': " + str(request.session["session"]) )
        else:
            request.session.set_expiry(60)
            request.session["session"] = "too reel"
            response.write( "Сохранил сессию: {'session': 'too reel'}" )

    except:

        response.write("<p>Exception: SESSION_ENGINE необходимо закоментировать в settings.py</p>")

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
    #url = "https://youtu.be/SszezOHLCCY"
    url = "https://www.prizmarket.ru"

    page = requests.get(url, headers=headers)

    #soup = BeautifulSoup(page.text, "html.parser")
    soup = BeautifulSoup(page.text, "lxml")

    #response.write( str(page.status_code)+"<br><br>"+str(soup.title.get_text())+"<br><br>" )
    response.write( str(page.status_code)+"<br><br>"+str(soup.body.get_text())+"<br><br>" )


    # деление ссылки на части и формирование новой
    '''
    split = url.split("/")
    length = len(split)
    response.write( "https://www.youtube.com/embed/" + str(split[length-1]) )
    '''

    # для titel с ютуба
    '''
    full_title = str(soup.title.get_text())
    num = full_title.find(" - YouTube")
    if num < 0:
        title = full_title
    else:
        title = full_title[:num]
    response.write( str(page.status_code)+"<br><br>"+title )
    '''

    return response

    ''' понял как передавать GET параметры

    query = {'q': 'Forest', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
    req = requests.get('https://pixabay.com/en/photos/', params=query)

    req.url
    # returns 'https://pixabay.com/en/photos/?order=popular&min_height=600&q=Forest&min_width=800'

    '''




def testjs(request):

    return render(request, "testjs/index.html")








