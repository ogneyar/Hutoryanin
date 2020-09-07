from django.http import HttpResponse
from django.http import HttpResponseRedirect

import requests
import json
import os
from bs4 import BeautifulSoup


def start(request):

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106",
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20200529.02.01'
    }

    #response = requests.get("https://www.youtube.com/watch?v=dGRJU_QlMf4&feature=youtu.be", headers=headers)

    url = "https://www.youtube.com/watch?v=dGRJU_QlMf4&feature=youtu.be"

    page = requests.get(url, headers=headers, timeout=(1, 3))

    response = tg.sendMessage(chat_id, "Статус код: \n\n" + str(page.status_code))

    soup = BeautifulSoup(page.text, "html.parser")

    return HttpResponse(soup.prettify())


    response = tg.sendMessage(chat_id, soup.title)

    div = soup.find(id="guide-button")

    response = tg.sendMessage(chat_id, repr(div))

    #return HttpResponse('<br><br><br><br><br><center>O da!</center>')



    '''
    h1_class_title = soup.findAll('h1', class_='title style-scope ytd-video-primary-info-renderer')

    response = tg.sendMessage(chat_id, repr(h1_class_title))
    '''

    #response = tg.sendMessage(chat_id, soup.body.find(id="description").span)

    #response = tg.sendMessage(chat_id, str(soup.find(id="description")))

    '''
    new_news = []
    news = []

    soup = BeautifulSoup(page.text, "html.parser")

    news = soup.findAll('div', class_='style-scope ytd-video-secondary-info-renderer')

    for i in range(len(news)):
        if news[i].find('span', class_='style-scope yt-formatted-string') is not None:
            new_news.append(news[i].text)

    for i in range(len(new_news)):
        response = tg.sendMessage(chat_id, new_news[i])
    '''
