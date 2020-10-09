# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Greeting, Url, Messages, Users


admin.site.register(Greeting)
admin.site.register(Url)
admin.site.register(Messages)
admin.site.register(Users)

