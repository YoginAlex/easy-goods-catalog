# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field photos on 'Item'
        db.delete_table(db.shorten_name(u'goods_item_photos'))

        # Adding field 'Photo.item'
        db.add_column(u'goods_photo', 'item',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', null=True, to=orm['goods.Item']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding M2M table for field photos on 'Item'
        m2m_table_name = db.shorten_name(u'goods_item_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'goods.item'], null=False)),
            ('photo', models.ForeignKey(orm[u'goods.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'photo_id'])

        # Deleting field 'Photo.item'
        db.delete_column(u'goods_photo', 'item_id')


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
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {}),
            'sizes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['goods.Size']", 'null': 'True', 'blank': 'True'}),
            'types': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goods.Type']", 'null': 'True', 'blank': 'True'})
        },
        u'goods.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'null': 'True', 'to': u"orm['goods.Item']"})
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