from django.shortcuts import render
#from django.http import HttpResponse

from .models import Greeting, Url

import os, bmemcached


def index(request):

    return render(request, "index.html")


def public(request):

    all_url = Url.objects.order_by('-id')

    return render(request, "public.html", {'all_url':all_url})


def shop(request):

    return render(request, "shop.html")


def promo(request):

    return render(request, "promo.html")


def about(request):

    return render(request, "about.html")


def support(request):
    
    mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
    mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
    mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')
    
    mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
    mc.enable_retry_delay(True)
    
    if mc.get("repeat") is not None:
        mc.delete("repeat")


    return render(request, "support.html")


def lk(request):

    return render(request, "lk.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



