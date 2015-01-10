# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buchung',
            name='buchung_habenKonto',
        ),
        migrations.RemoveField(
            model_name='buchung',
            name='buchung_sollKonto',
        ),
        migrations.AlterField(
            model_name='konto',
            name='konto_id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
