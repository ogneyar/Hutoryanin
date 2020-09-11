from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Url

import requests


def index(request):

    return render(request, "index.html")


def public(request):

    all_url = Url.objects.all()

    return render(request, "public.html", {'all_url':all_url})


def shop(request):

    return render(request, "shop.html")


def promo(request):

    return render(request, "promo.html")


def about(request):

    return render(request, "about.html")


def support(request):

    return render(request, "support.html")


def lk(request):

    return render(request, "lk.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



