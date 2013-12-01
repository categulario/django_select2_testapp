# -*- coding:utf-8 -*-
from django.contrib import admin
from someapp.models import *
from someapp.forms import *

class BazAdmin(admin.ModelAdmin):
    form = BazForm

    class Media:
        js = ['jquery-1.7.2.min.js']

admin.site.register(Baz, BazAdmin)