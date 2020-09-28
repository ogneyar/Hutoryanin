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
    path("vanila/", bots.views.vanila, name="vanila"),
    path("fullPageScrolling/", bots.views.fullPageScrolling, name="fullPageScrolling"),
]
