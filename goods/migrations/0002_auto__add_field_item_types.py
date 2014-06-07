# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.types'
        db.add_column(u'goods_item', 'types',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goods.Type'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field types on 'Item'
        db.delete_table(db.shorten_name(u'goods_item_types'))


    def backwards(self, orm):
        # Deleting field 'Item.types'
        db.delete_column(u'goods_item', 'types_id')

        # Adding M2M table for field types on 'Item'
        m2m_table_name = db.shorten_name(u'goods_item_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'goods.item'], null=False)),
            ('type', models.ForeignKey(orm[u'goods.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'type_id'])


    models = {
        u'goods.color': {
            'Meta': {'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'goods.item': {
            'Meta': {'object_name': 'Item'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['goods.Color']", 'symmetrical': 'False'}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['goods.Photo']", 'symmetrical': 'False'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'show': ('django.db.models.fields.BooleanField', [], {}),
            'sizes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['goods.Size']", 'symmetrical': 'False'}),
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