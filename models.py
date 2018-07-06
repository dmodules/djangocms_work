# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(_('Name'), max_length=200)# (requis)
    description = models.TextField(_('Description'), null=True,blank=True) 

    def __unicode__(self):
        return self.nom

class Work(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(_('Name'), max_length=200)# (requis)
    description = models.TextField(_('Description'), null=True,blank=True) 

    def __unicode__(self):
        return self.nom
