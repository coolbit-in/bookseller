#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os, sys
setting_path = os.path.join(os.path.dirname(__file__), 'bookseller')
#sys.path += str(setting_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookseller.settings")

from bookseller.apps.main import models

tag_list = ['课本', '课外书', '数码产品', '数码外设', '家居用品', '服装鞋子', '体育用品', '其他']
for tag in tag_list:
    models.Tags(name=tag).save()
