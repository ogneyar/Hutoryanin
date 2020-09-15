#!/usr/bin/python3

from django.http import HttpResponse
from django.http import HttpResponseRedirect


def send(request):

   return HttpResponse("<h1>Добро пожаловать!</h1>")


