# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Registration.push_token'
        db.alter_column(u'django_passbook_registration', 'push_token', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'Registration.device_library_identifier'
        db.alter_column(u'django_passbook_registration', 'device_library_identifier', self.gf('django.db.models.fields.CharField')(max_length=64))

    def backwards(self, orm):

        # Changing field 'Registration.push_token'
        db.alter_column(u'django_passbook_registration', 'push_token', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Registration.device_library_identifier'
        db.alter_column(u'django_passbook_registration', 'device_library_identifier', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'django_passbook.log': {
            'Meta': {'object_name': 'Log'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        },
        u'django_passbook.pass': {
            'Meta': {'unique_together': "(('pass_type_identifier', 'serial_number'),)", 'object_name': 'Pass'},
            'authentication_token': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'data': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pass_type_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'django_passbook.registration': {
            'Meta': {'object_name': 'Registration'},
            'device_library_identifier': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pazz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_passbook.Pass']"}),
            'push_token': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['django_passbook']