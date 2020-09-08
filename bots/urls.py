"""hutoryanin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

import bots.test

# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", bots.test.test, name="test"),
    path("getcookie/", bots.test.getCookie, name="getCookie"),
    path("cookie/", bots.test.cookie, name="cookie"),
    path("session/", bots.test.session, name="session"),
    path("parser/", bots.test.parser, name="parser"),
]
