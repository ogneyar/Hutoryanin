# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, Textarea
from .models import Url
from .models import Messages
from .models import Users


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['title','url','file_id']

        widgets = {
            "title":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи название'
            }),
            "url":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи ссылку'
            }),
            "file_id":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи file_id'
            })
        }


class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['email','text']

        widgets = {
            "email":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваш Email',
                'name': "email",
                'id': "email",
                'maxlength': "100"
            }),
            "text":Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Здесь напишите Ваш вопрос или предложение',
                'name': "message",
                'id': "message",
                'maxlength': "1500"
            })
        }


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['login','password','email','adress','promo','info']

        widgets = {
            "login":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи название',
                'name': "login",
                'id': "login",
                'maxlength': "100"
            }),
            "password":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи пароль',
                'name': "password",
                'id': "password",
                'maxlength': "100"
            }),
            "email":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи email',
                'name': "email",
                'id': "email",
                'maxlength': "100"
            }),
            "adress":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи адрес с индексом',
                'name': "adress",
                'id': "adress",
                'maxlength': "100"
            }),
            "promo":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи promo-код',
                'name': "promo",
                'id': "promo",
                'maxlength': "100"
            }),
            "info":Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Доп. информация',
                'name': "info",
                'id': "info",
                'maxlength': "1500"
            })
        }
