# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilanz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='konto',
            name='konto_type3',
            field=models.CharField(choices=[('UV', 'Umlaufvermögen'), ('AV', 'Anlagevermögen'), ('kFK', 'kurzfristiges Fremdkapital'), ('lFK', 'langfristiges Fremdkapital'), ('EK', 'Steuer')], max_length=3, default='UV'),
            preserve_default=False,
        ),
    ]
