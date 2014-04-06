#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os, sys
setting_path = os.path.join(os.path.dirname(__file__), 'bookseller')
#sys.path += str(setting_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookseller.settings")

from bookseller.apps.main import models
models.Tags(name='书籍').save()
models.Tags(name='家电').save()
models.Tags(name='用品').save()
