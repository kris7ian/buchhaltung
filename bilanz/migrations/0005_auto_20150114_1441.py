# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0004_konto_konto_erfolgswirksam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tag_tag', models.CharField(max_length=80, verbose_name='Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='konto',
            name='konto_tag',
            field=models.ForeignKey(to='bilanz.Tag', related_name='tag', default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='konto',
            name='konto_type2',
            field=models.CharField(default='-', choices=[('-', 'nicht erfolgswirksam'), ('Betrieb', 'Betrieb'), ('Finanz', 'Finanz'), ('Neutral', 'Neutral'), ('Steuer', 'Steuer')], max_length=1),
            preserve_default=True,
        ),
    ]
