from django.shortcuts import render
from django.http import Http404

from .models import Greeting, Url

import os, bmemcached


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

    return render(request, "public.html", {
        'all_url':all_url,
        'quan_page':range(int(quantity)+1),
        'page_id':0
    })


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

    return render(request, "public.html", {
        'all_url':all_url,
        'quan_page':range(int(quantity)+1),
        'page_id':page_id
    })


def shop(request):

    return render(request, "shop.html")


def promo(request):

    return render(request, "promo.html")


def about(request):

    return render(request, "about.html")


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


    return render(request, "support.html")


def lk(request):

    return render(request, "lk.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



