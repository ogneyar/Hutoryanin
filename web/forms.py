# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput
from .models import Url


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


