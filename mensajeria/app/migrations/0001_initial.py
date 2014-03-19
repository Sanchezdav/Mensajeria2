# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'app_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('numero_servidor', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Usuario'])

        # Adding model 'Status'
        db.create_table(u'app_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Status'])

        # Adding model 'Notificador'
        db.create_table(u'app_notificador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apePaterno', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('apeMaterno', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('statusNotificador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Status'])),
        ))
        db.send_create_signal(u'app', ['Notificador'])

        # Adding model 'Sitio'
        db.create_table(u'app_sitio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('referencia', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Sitio'])

        # Adding model 'TipoServicio'
        db.create_table(u'app_tiposervicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoServicio', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'app', ['TipoServicio'])

        # Adding model 'Servicio'
        db.create_table(u'app_servicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('solicitante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('notificador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Notificador'])),
            ('fechaInicio', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fechaEnterado', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('fechaFin', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sitio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Sitio'])),
            ('actividad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.TipoServicio'])),
            ('comentarios', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Servicio'])


    def backwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table(u'app_usuario')

        # Deleting model 'Status'
        db.delete_table(u'app_status')

        # Deleting model 'Notificador'
        db.delete_table(u'app_notificador')

        # Deleting model 'Sitio'
        db.delete_table(u'app_sitio')

        # Deleting model 'TipoServicio'
        db.delete_table(u'app_tiposervicio')

        # Deleting model 'Servicio'
        db.delete_table(u'app_servicio')


    models = {
        u'app.notificador': {
            'Meta': {'object_name': 'Notificador'},
            'apeMaterno': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'apePaterno': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'statusNotificador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Status']"})
        },
        u'app.servicio': {
            'Meta': {'object_name': 'Servicio'},
            'actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.TipoServicio']"}),
            'comentarios': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fechaEnterado': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fechaFin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fechaInicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notificador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Notificador']"}),
            'sitio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Sitio']"}),
            'solicitante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'app.sitio': {
            'Meta': {'object_name': 'Sitio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'referencia': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'app.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.tiposervicio': {
            'Meta': {'object_name': 'TipoServicio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoServicio': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'app.usuario': {
            'Meta': {'object_name': 'Usuario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_servidor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']