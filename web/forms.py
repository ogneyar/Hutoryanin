# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput
from .models import Url


class UrlForms(ModelForm):
    class Meta:
        models = Url
        fields = ['title','url','file_id']

    widgets = {
        "title":TextInput(attr={
            'class': 'form-control'
            'placeholder': 'Введи название'
        }),
        "url":TextInput(attr={
            'class': 'form-control'
            'placeholder': 'Введи ссылку'
        }),
        "file_id":TextInput(attr={
            'class': 'form-control'
            'placeholder': 'Введи file_id'
        })
    }
    
