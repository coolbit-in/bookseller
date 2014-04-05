#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.forms import ModelForm
from bookseller.apps.main.models import Tags, Item, Messages, Image

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price',
                  'number', 'tag', 'status']