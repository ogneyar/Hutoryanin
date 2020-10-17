from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

import web.views
import web.templates.support.sendmail

import bots.tgbot
import bots.icqbot
import bots.urls


urlpatterns = [
    path("", web.views.index, name="index"),

    path("public/", web.views.public, name="public"),
    path("public/<int:page_id>/", web.views.public_page, name="public_page"),

    path("products/", web.views.products, name="products"),
    path("products/<str:category>/<str:product>/creating_an_order", web.views.creating_an_order, name="creating_an_order"),

    path("products/knives/", web.views.knives, name="knives"),
    path("products/knives/low_knife", web.views.low_knife, name="low_knife"),
    path("products/knives/middle_knife", web.views.middle_knife, name="middle_knife"),
    path("products/knives/high_knife", web.views.high_knife, name="high_knife"),

    path("products/spoons/", web.views.spoons, name="spoons"),
    path("products/spoons/low_spoon/", web.views.low_spoon, name="low_spoon"),
    path("products/spoons/middle_spoon/", web.views.middle_spoon, name="middle_spoon"),
    path("products/spoons/high_spoon/", web.views.high_spoon, name="high_spoon"),

    path("products/candlesticks/", web.views.candlesticks, name="candlesticks"),
    path("products/candlesticks/low_candlestick", web.views.low_candlestick, name="low_candlestick"),
    path("products/candlesticks/middle_candlestick", web.views.middle_candlestick, name="middle_candlestick"),
    path("products/candlesticks/high_candlestick", web.views.high_candlestick, name="high_candlestick"),

    path("products/applications/", web.views.applications, name="applications"),
    path("products/applications/site", web.views.site, name="site"),
    path("products/applications/tgbot", web.views.tgbot, name="tgbot"),
    path("products/applications/vkbot", web.views.vkbot, name="vkbot"),
    path("products/applications/android", web.views.android, name="android"),

    path("promo/", web.views.promo, name="promo"),

    path("support/", web.views.support, name="support"),
    path("sendmail/", web.templates.support.sendmail.send, name="send"),

    path("lk/", web.views.lk, name="lk"),
    path("exit/", web.views.exit, name="exit"),
    path("registration/", web.views.registration, name="registration"),
    path("forget_password/", web.views.forget_password, name="forget_password"),


    path("about/", web.views.about, name="about"),
    path("db/", web.views.db, name="db"),


    path("tgbot/", bots.tgbot.bot, name="bot"),
    path("icqbot/", bots.icqbot.message_cb, name="message_cb"),

    path("test/", include("bots.urls")),


]
