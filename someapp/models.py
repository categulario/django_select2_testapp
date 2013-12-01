# -*- coding:utf-8 -*-
from django.db import models

class Foo(models.Model):
    name    = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Baz(models.Model):
    foo     = models.ForeignKey(Foo, null=True, blank=True)
    name    = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name