from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests


def index(request):

    return render(request, "index.html")


def shop(request):

    return render(request, "shop.html")


def promo(request):

    return render(request, "promo.html")


def about(request):

    return render(request, "about.html")


def support(request):

    return render(request, "support.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



