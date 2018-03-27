# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..loginapp.models import Users

# Create your models here.
class Janitor(models.Manager):
    def polish(self,postData):
        errors= []
        if len(postData['name']) < 3:
            errors.append('Your item must be larger than 3 Characters')
        return errors

class Wish(models.Model):
    name = models.CharField(max_length = 255)
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Users, related_name="created_by")
    join = models.ManyToManyField(Users, related_name="items_wanted")

    objects=Janitor()


