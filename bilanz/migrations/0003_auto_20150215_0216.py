# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0002_konto_konto_type3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buchung',
            name='buchung_amount',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
