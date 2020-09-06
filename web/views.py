from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests


def index(request):

    return render(request, "index.html")

    #response =  requests.get("https://api.telegram.org/bot1334552817:AAG4qshVQSht2JoWzovwqQ7u2PSOjZVYrlY/sendMessage?chat_id=1038937592&text=Вооот ")
    #return HttpResponse('<br><br><br><br><br><center>Hello from Python!</center>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def shop(request):

    return render(request, "shop.html")

def support(request):

    return render(request, "support.html")
