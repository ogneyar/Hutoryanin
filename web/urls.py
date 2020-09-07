"""hutoryanin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

import web.views
import bots.tgbot
import bots.icqbot
import bots.test

# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", web.views.index, name="index"),
    path("shop/", web.views.shop, name="shop"),
    path("promo/", web.views.promo, name="promo"),
    path("about/", web.views.about, name="about"),
    path("support/", web.views.support, name="support"),
    path("lk/", web.views.lk, name="lk"),

    path("test/", bots.test.start, name="test"),
    path("db/", web.views.db, name="db"),

    path("tgbot/", bots.tgbot.bot, name="bot"),
    path("icqbot/", bots.icqbot.message_cb, name="message_cb"),
]
