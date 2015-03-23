# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0006_auto_20150216_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='konto',
            name='konto_currency',
            field=models.CharField(choices=[('CHF', 'CHF'), ('EUR', 'EUR'), ('USD', 'USD')], default='CHF', max_length=3),
            preserve_default=True,
        ),
    ]
