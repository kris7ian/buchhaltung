# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0007_auto_20150114_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konto',
            name='konto_type2',
            field=models.CharField(choices=[('-', 'nicht erfolgswirksam'), ('B', 'Betrieb'), ('F', 'Finanz'), ('N', 'Neutral'), ('S', 'Steuer')], default='-', max_length=1),
            preserve_default=True,
        ),
    ]
