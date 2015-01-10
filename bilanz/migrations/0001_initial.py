# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buchung',
            fields=[
                ('buchung_id', models.AutoField(serialize=False, primary_key=True)),
                ('buchung_descr', models.CharField(max_length=128, verbose_name='Description')),
                ('buchung_amount', models.IntegerField(default=0)),
                ('buchung_date', models.DateTimeField(verbose_name='Buchungsdatum')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('konto_title', models.CharField(max_length=200)),
                ('konto_id', models.IntegerField(serialize=False, primary_key=True)),
                ('konto_anfangsBestand', models.IntegerField(default=0)),
                ('konto_sum', models.IntegerField(default=0)),
                ('konto_type', models.CharField(max_length=1, choices=[('A', 'Aktiv'), ('P', 'Passiv')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='buchung',
            name='buchung_habenKonto',
            field=models.ManyToManyField(related_name='habenKonto', to='bilanz.Konto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buchung',
            name='buchung_sollKonto',
            field=models.ManyToManyField(related_name='sollKonto', to='bilanz.Konto'),
            preserve_default=True,
        ),
    ]
