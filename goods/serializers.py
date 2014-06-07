# -*- coding: utf-8 -*-
from rest_framework import serializers
from goods.models import *

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type

class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.Field('image.url')

    class Meta:
        model = Photo

class ItemSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(required=False)
    types = TypeSerializer(required=False)
    sizes = SizeSerializer(required=False)
    photos = PhotoSerializer(required=False)

    class Meta:
        model = Item

