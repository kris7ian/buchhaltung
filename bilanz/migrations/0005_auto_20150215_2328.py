# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0004_auto_20150215_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='konto',
            name='konto_anfangsBestand',
        ),
        migrations.RemoveField(
            model_name='konto',
            name='konto_sum',
        ),
    ]
