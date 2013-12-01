# -*- coding:utf-8 -*-
from django import forms
from django_select2 import *
from someapp.models import *

class FooSingeChoice(AutoModelSelect2Field):
    queryset = Foo.objects
    search_fields = ['name__icontains',]

class BazForm(forms.ModelForm):
    foo         = FooSingeChoice()

    class Meta:
        model = Baz