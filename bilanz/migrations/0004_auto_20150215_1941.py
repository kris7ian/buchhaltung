# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('bilanz', '0003_auto_20150215_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tag_tag', models.CharField(max_length=80, verbose_name='Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='buchung',
            name='buchung_tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', blank=True, to='taggit.Tag', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
