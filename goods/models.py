# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Color(models.Model):
    """
    Модель цветов товаров.
    Заполняется из стандартной Django админки.
    """
    name = models.CharField(max_length=200)

class Size(models.Model):
    """
    Модель размеров товаров.
    Заполняется из стандартной Django админки.
    """
    name = models.CharField(max_length=200)

class Type(models.Model):
    """
    Модель разделов/типов товаров.
    Заполняется из стандартной Django админки.
    """
    name = models.CharField(max_length=200)

class Photo(models.Model):
    """
    Модель фоток товаров.
    """
    image = models.ImageField(upload_to="/photos")

class Item(models.Model):
    """
    Модель товаров.
    """
    add_date = models.DateTimeField(default=datetime.now, blank=True)
    name = models.CharField(max_length=200)
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    types = models.ManyToManyField(Type)
    photos = models.ManyToManyField(Photo)
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.TextField()
    show = models.BooleanField() # Показывать ли на сайте
