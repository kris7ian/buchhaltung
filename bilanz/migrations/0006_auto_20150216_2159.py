# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bilanz', '0005_auto_20150215_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='buchung',
            name='buchung_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='konto',
            name='konto_type3',
            field=models.CharField(max_length=3, choices=[('-', 'erfolgswirksam'), ('UV', 'Umlaufvermoegen'), ('AV', 'Anlagevermoegen'), ('kFK', 'kurzfristiges Fremdkapital'), ('lFK', 'langfristiges Fremdkapital'), ('EK', 'Eigenkapital')]),
            preserve_default=True,
        ),
    ]
