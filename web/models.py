# -*- coding: utf-8 -*-
from django.db import models


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Url(models.Model):
    title = models.CharField("Название видео", max_length=200)
    url = models.CharField("Ссылка на видео", max_length=200)
    file_id = models.CharField("Номер файла в телеграм", max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылка'


class Messages(models.Model):
    email = models.CharField("email", max_length=200)
    text = models.TextField("Текст сообщения")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщение'



