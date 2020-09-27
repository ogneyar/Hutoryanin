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

def creating_an_order(request, category, product):

    return render(request, "products/creating_an_order.html", {'category':category,'product':product})

def knives(request):

    return render(request, "products/knives/knives.html")

def low_knife(request):

    return render(request, "products/knives/low_knife.html")

def middle_knife(request):

    return render(request, "products/knives/middle_knife.html")

def high_knife(request):

    return render(request, "products/knives/high_knife.html")

def spoons(request):

    return render(request, "products/spoons/spoons.html")

def low_spoon(request):

    return render(request, "products/spoons/low_spoon.html")

def middle_spoon(request):

    return render(request, "products/spoons/middle_spoon.html")

def high_spoon(request):

    return render(request, "products/spoons/high_spoon.html")

def candlesticks(request):

    return render(request, "products/candlesticks/candlesticks.html")

def low_candlestick(request):

    return render(request, "products/candlesticks/low_candlestick.html")

def middle_candlestick(request):

    return render(request, "products/candlesticks/middle_candlestick.html")

def high_candlestick(request):

    return render(request, "products/candlesticks/high_candlestick.html")


def applications(request):

    return render(request, "products/applications/applications.html")

def site(request):

    return render(request, "products/applications/site.html")

def tgbot(request):

    return render(request, "products/applications/tgbot.html")

def android(request):

    return render(request, "products/applications/android.html")



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

    return render(request, "support/support.html")


def lk(request):

    return render(request, "lk.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def prizm(request):

    return render(request, "prizm/prizm.html")

def vanila(request):

    return render(request, "prizm/vanila.html")


