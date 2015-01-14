# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0005_auto_20150114_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konto',
            name='konto_tag',
            field=models.ForeignKey(to='bilanz.Tag', related_name='tag'),
            preserve_default=True,
        ),
    ]
