#!/usr/bin/python3

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

import os, smtplib, requests, json, bmemcached

from classes.tg.botApi import Bot


mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
mc_passw = os.environ.get('MEMCACHIER_PASSWORD', '')

mc = bmemcached.Client(mc_servers, username=mc_user, password=mc_passw)
mc.enable_retry_delay(True)


def support(request):
    
    token = os.getenv("TOKEN")
    master = int(os.getenv("MASTER"))
    
    tg = Bot(token)

    r = tg.sendMessage(master, "eee")
    
    if mc.get("repeat") is not None:
        mc.delete("repeat")
      
            
    return render(request, "support.html")
    
