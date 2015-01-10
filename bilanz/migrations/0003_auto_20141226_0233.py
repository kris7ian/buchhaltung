# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0002_auto_20141226_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='buchung',
            name='buchung_habenKonto',
            field=models.ForeignKey(to='bilanz.Konto', default=0, related_name='habenKonto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buchung',
            name='buchung_sollKonto',
            field=models.ForeignKey(to='bilanz.Konto', default=0, related_name='sollKonto'),
            preserve_default=False,
        ),
    ]
