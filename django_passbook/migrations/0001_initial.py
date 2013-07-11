# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pass'
        db.create_table(u'django_passbook_pass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pass_type_identifier', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('authentication_token', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('data', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'django_passbook', ['Pass'])

        # Adding unique constraint on 'Pass', fields ['pass_type_identifier', 'serial_number']
        db.create_unique(u'django_passbook_pass', ['pass_type_identifier', 'serial_number'])

        # Adding model 'Registration'
        db.create_table(u'django_passbook_registration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device_library_identifier', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('push_token', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pazz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_passbook.Pass'])),
        ))
        db.send_create_signal(u'django_passbook', ['Registration'])

        # Adding model 'Log'
        db.create_table(u'django_passbook_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'django_passbook', ['Log'])


    def backwards(self, orm):
        # Removing unique constraint on 'Pass', fields ['pass_type_identifier', 'serial_number']
        db.delete_unique(u'django_passbook_pass', ['pass_type_identifier', 'serial_number'])

        # Deleting model 'Pass'
        db.delete_table(u'django_passbook_pass')

        # Deleting model 'Registration'
        db.delete_table(u'django_passbook_registration')

        # Deleting model 'Log'
        db.delete_table(u'django_passbook_log')


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
            'device_library_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pazz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_passbook.Pass']"}),
            'push_token': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['django_passbook']