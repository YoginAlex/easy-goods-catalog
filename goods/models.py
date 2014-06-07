# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.conf import settings

class Color(models.Model):
    """
    Модель цветов товаров.
    Заполняется из стандартной Django админки.
    """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Size(models.Model):
    """
    Модель размеров товаров.
    Заполняется из стандартной Django админки.
    """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Type(models.Model):
    """
    Модель разделов/типов товаров.
    Заполняется из стандартной Django админки.
    """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    """
    Модель фоток товаров.
    """
    image = models.ImageField(null=True, upload_to="photos")

class Item(models.Model):
    """
    Модель товаров.
    """
    add_date = models.DateTimeField(default=datetime.now, blank=True)
    name = models.CharField(max_length=200)
    colors = models.ManyToManyField(Color, blank=True, null=True)
    sizes = models.ManyToManyField(Size, blank=True, null=True)
    types = models.ForeignKey(Type, blank=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField() # Показывать ли на сайте

    def __unicode__(self):
        return self.name
