# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Knight.plays_football'
        db.add_column(u'b11_test_knight', 'plays_football',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Knight.plays_football'
        db.delete_column(u'b11_test_knight', 'plays_football')


    models = {
        u'b11_test.knight': {
            'Meta': {'object_name': 'Knight'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {}),
            'plays_football': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['b11_test']