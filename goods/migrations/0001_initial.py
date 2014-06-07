# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Color'
        db.create_table(u'goods_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'goods', ['Color'])

        # Adding model 'Size'
        db.create_table(u'goods_size', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'goods', ['Size'])

        # Adding model 'Type'
        db.create_table(u'goods_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'goods', ['Type'])

        # Adding model 'Photo'
        db.create_table(u'goods_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'goods', ['Photo'])

        # Adding model 'Item'
        db.create_table(u'goods_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('show', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'goods', ['Item'])

        # Adding M2M table for field colors on 'Item'
        m2m_table_name = db.shorten_name(u'goods_item_colors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'goods.item'], null=False)),
            ('color', models.ForeignKey(orm[u'goods.color'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'color_id'])

        # Adding M2M table for field sizes on 'Item'
        m2m_table_name = db.shorten_name(u'goods_item_sizes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'goods.item'], null=False)),
            ('size', models.ForeignKey(orm[u'goods.size'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'size_id'])

        # Adding M2M table for field types on 'Item'
        m2m_table_name = db.shorten_name(u'goods_item_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'goods.item'], null=False)),
            ('type', models.ForeignKey(orm[u'goods.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'type_id'])

        # Adding M2M table for field photos on 'Item'
        m2m_table_name = db.shorten_name(u'goods_item_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'goods.item'], null=False)),
            ('photo', models.ForeignKey(orm[u'goods.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'photo_id'])


    def backwards(self, orm):
        # Deleting model 'Color'
        db.delete_table(u'goods_color')

        # Deleting model 'Size'
        db.delete_table(u'goods_size')

        # Deleting model 'Type'
        db.delete_table(u'goods_type')

        # Deleting model 'Photo'
        db.delete_table(u'goods_photo')

        # Deleting model 'Item'
        db.delete_table(u'goods_item')

        # Removing M2M table for field colors on 'Item'
        db.delete_table(db.shorten_name(u'goods_item_colors'))

        # Removing M2M table for field sizes on 'Item'
        db.delete_table(db.shorten_name(u'goods_item_sizes'))

        # Removing M2M table for field types on 'Item'
        db.delete_table(db.shorten_name(u'goods_item_types'))

        # Removing M2M table for field photos on 'Item'
        db.delete_table(db.shorten_name(u'goods_item_photos'))


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
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['goods.Type']", 'symmetrical': 'False'})
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