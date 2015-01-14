# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0006_auto_20150114_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='konto',
            name='konto_tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
