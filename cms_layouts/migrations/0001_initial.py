# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('layout_type', models.IntegerField(default=0)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('from_page', models.ForeignKey(to='cms.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LayoutPlaceholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('holder', models.ForeignKey(to='cms.Placeholder')),
                ('layout', models.ForeignKey(related_name='placeholders', to='cms_layouts.Layout')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
