# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.description'
        db.alter_column(u'goods_item', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Item.cost'
        db.alter_column(u'goods_item', 'cost', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Item.quantity'
        db.alter_column(u'goods_item', 'quantity', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Item.description'
        db.alter_column(u'goods_item', 'description', self.gf('django.db.models.fields.TextField')(default=datetime.datetime(2014, 6, 7, 0, 0)))

        # Changing field 'Item.cost'
        db.alter_column(u'goods_item', 'cost', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'Item.quantity'
        db.alter_column(u'goods_item', 'quantity', self.gf('django.db.models.fields.IntegerField')(default=1))

    models = {
        u'goods.color': {
            'Meta': {'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'goods.item': {
            'Meta': {'object_name': 'Item'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['goods.Color']", 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['goods.Photo']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {}),
            'sizes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['goods.Size']", 'null': 'True', 'blank': 'True'}),
            'types': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goods.Type']", 'null': 'True', 'blank': 'True'})
        },
        u'goods.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'goods.size': {
            'Meta': {'object_name': 'Size'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'goods.type': {
            'Meta': {'object_name': 'Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['goods']