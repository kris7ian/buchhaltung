from django.db import models


class Konto(models.Model):
    konto_title = models.CharField(max_length=200)
    konto_id = models.AutoField(primary_key=True) #actually AutoField is safer
    konto_anfangsBestand = models.IntegerField(default=0)
    konto_sum = models.IntegerField(default=0)
    konto_types = (
        ('A', 'Aktiv'),
        ('P', 'Passiv')
    )
    konto_type = models.CharField(max_length=1, choices=konto_types)
    def __str__(self):
        return self.konto_title


class Buchung(models.Model):
    buchung_id = models.AutoField(primary_key=True)
    buchung_descr = models.CharField('Description', max_length=128)
    buchung_amount = models.IntegerField(default=0)
    buchung_sollKonto = models.ForeignKey(Konto, related_name='sollKonto')
    buchung_habenKonto = models.ForeignKey(Konto, related_name='habenKonto')
    buchung_date = models.DateTimeField('Buchungsdatum')
    def __str__(self):
        return self.buchung_descr
