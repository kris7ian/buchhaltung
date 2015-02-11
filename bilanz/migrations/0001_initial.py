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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('buchung_descr', models.CharField(max_length=128, verbose_name='Description')),
                ('buchung_amount', models.IntegerField(default=0)),
                ('buchung_date', models.DateField(verbose_name='Buchungsdatum')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('konto_title', models.CharField(max_length=200)),
                ('konto_anfangsBestand', models.IntegerField(default=0)),
                ('konto_sum', models.IntegerField(default=0)),
                ('konto_erfolgswirksam', models.BooleanField(default=False)),
                ('konto_type', models.CharField(choices=[('A', 'Aktiv'), ('P', 'Passiv')], max_length=1)),
                ('konto_type2', models.CharField(choices=[('-', 'nicht erfolgswirksam'), ('B', 'Betrieb'), ('F', 'Finanz'), ('N', 'Neutral'), ('S', 'Steuer')], default='-', max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='buchung',
            name='buchung_habenKonto',
            field=models.ForeignKey(related_name='habenKonto', to='bilanz.Konto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buchung',
            name='buchung_sollKonto',
            field=models.ForeignKey(related_name='sollKonto', to='bilanz.Konto'),
            preserve_default=True,
        ),
    ]
