"""hutoryanin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

import web.views
import web.templates.support.sendmail

import bots.tgbot
import bots.icqbot
import bots.urls

# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", web.views.index, name="index"),

    path("public/", web.views.public, name="public"),
    path("public/<int:page_id>/", web.views.public_page, name="public_page"),

    path("shop/", web.views.shop, name="shop"),
    path("shop/<str:product>/", web.views.creating_an_order, name="creating_an_order"),

    path("support/", web.views.support, name="support"),
    path("sendmail/", web.templates.support.sendmail.send, name="send"),

    path("promo/", web.views.promo, name="promo"),

    path("about/", web.views.about, name="about"),
    path("lk/", web.views.lk, name="lk"),
    path("db/", web.views.db, name="db"),


    path("tgbot/", bots.tgbot.bot, name="bot"),
    path("icqbot/", bots.icqbot.message_cb, name="message_cb"),

    path("test/", include("bots.urls")),
]
