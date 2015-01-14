# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0003_auto_20141226_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='konto',
            name='konto_erfolgswirksam',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
