#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django import forms
from bookseller.apps.main.models import Tags, Item, Messages, Image

class ItemCreateForm(forms.Form):
    title = forms.CharField(max_length= 256)
    description = forms.CharField()
    price = forms.FloatField(min_value=0)
    number = forms.IntegerField(min_value=1)
    image = forms.ImageField(required=False)
    tags = forms.IntegerField(min_value=1)

class ItemUpdateForm(forms.Form):
    description = forms.CharField()
    price = forms.FloatField(min_value=0)
    number = forms.IntegerField(min_value=1)
    image = forms.ImageField(required=False)
