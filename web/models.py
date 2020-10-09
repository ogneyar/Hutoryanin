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
        verbose_name = 'Ссылку'
        verbose_name_plural = 'Ссылки'


class Messages(models.Model):
    email = models.CharField("email", max_length=200)
    text = models.TextField("Текст сообщения")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Users(models.Model):
    login = models.CharField("login", max_length=200)
    password = models.CharField("password", max_length=200)
    email = models.CharField("email", max_length=200)
    adress = models.CharField("adress", max_length=500)
    promo = models.CharField("promo", max_length=200)
    info = models.TextField("Текст сообщения")

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


