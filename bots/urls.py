from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

import bots.test
import bots.views


urlpatterns = [
    path("", bots.test.test, name="test"),
    path("getcookie/", bots.test.getCookie, name="getCookie"),
    path("cookie/", bots.test.cookie, name="cookie"),
    path("session/", bots.test.session, name="session"),
    path("parser/", bots.test.parser, name="parser"),

    path("prizm/", bots.views.prizm, name="prizm"),
    path("7yanika/", bots.views.semyanika, name="7yanika"),
    path("hutor/", bots.views.hutor, name="hutor"),

    path("vanilla/", bots.views.vanilla, name="vanilla"),
    path("fullPageScrolling/", bots.views.fullPageScrolling, name="fullPageScrolling"),
    path("neonButton/", bots.views.neonButton, name="neonButton"),
    path("sidebarMenu/", bots.views.sidebarMenu, name="sidebarMenu"),
    path("cardHoverEffects/", bots.views.cardHoverEffects, name="cardHoverEffects"),

]
