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
    image = models.ImageField(null=True, upload_to="photos", blank=True)
    # item = models.ForeignKey()

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
    image_thumb.allow_tags = True

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

    def image_thumb(self):
        try: 
            self.photos.all()[0]
        except:
            return u'No photo'
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.photos.all()[0].image)

    def colors_list(self):
        try:
            self.colors.all()[0]
        except:
            return u'-'
        else:
            colors_list = ''
            for obj in self.colors.all():
                colors_list = colors_list + obj.name +', '
            return colors_list[:-2]

    def sizes_list(self):
        try:
            self.sizes.all()[0]
        except:
            return u'-'
        else:
            sizes_list = ''
            for obj in self.sizes.all():
                sizes_list = sizes_list + obj.name +', '
            return sizes_list[:-2]

    image_thumb.allow_tags = True
    colors_list.allow_tags = True
    sizes_list.allow_tags = True
