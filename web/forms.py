# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, Textarea
from .models import Url
from .models import Messages


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

