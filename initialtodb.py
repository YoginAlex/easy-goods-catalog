# -*- coding: utf-8 -*-
import os
import os.path
import random

from django.conf import settings

from goods.models import *


colors = [u'Красный', u'Синий', u'Зеленый']
for color in colors:
    Color.objects.create(name=color)

sizes = [u'XS', u'S', u'M', u'L', u'XL']
for size in sizes:
    Size.objects.create(name=size)

types = [u'Трусы', u'Носки', u'Куртки', u'Шорты']
for ttype in types:
    Type.objects.create(name=ttype)

for i in range(1, 50):
    item_name = u'Товар_' + str(i)
    colors = Color.objects.all().order_by('?')[:2]
    sizes = Size.objects.all().order_by('?')[:2]
    types = Type.objects.all().order_by('?')[0]

    item = Item(
        name=item_name,
        types=types,
        quantity=random.randint(0, 50),
        cost=random.randint(100, 900),
        description=u'Lorem ipsum dolor sit amet, '
                    u'consectetur adipisicing elit. Nulla, totam '
                    u'cumque delectus fuga veritatis ipsa nisi. '
                    u'Expedita, molestiae, aspernatur pariatur '
                    u'sequi autem voluptatibus repellat laborum '
                    u'delectus similique laudantium incidunt consequuntur!',
        show=random.choice([True, False])
    )
    item.save()
    for size in sizes:
        item.sizes.add(size)
    for color in colors:
        item.colors.add(color)
    item.save()
