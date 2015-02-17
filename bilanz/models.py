from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Tag(models.Model):
    tag_tag = models.CharField('Tag', max_length=80)
    def __str__(self):
        return self.tag_tag

class Konto(models.Model):
    konto_title = models.CharField(max_length=200)
    konto_erfolgswirksam = models.BooleanField(default=False)
    konto_types = (
        ('A', 'Aktiv'),
        ('P', 'Passiv')
    )
    konto_types2 = (
        ('-', 'nicht erfolgswirksam'),
        ('B', 'Betrieb'),
        ('F', 'Finanz'),
        ('N', 'Neutral'),
        ('S', 'Steuer'),
    )
    konto_types3 = (
        ('-', 'erfolgswirksam'),
        ('UV', 'Umlaufvermoegen'),
        ('AV', 'Anlagevermoegen'),
        ('kFK', 'kurzfristiges Fremdkapital'),
        ('lFK', 'langfristiges Fremdkapital'),
        ('EK', 'Eigenkapital'),
    )
    konto_type = models.CharField(max_length=1, choices=konto_types)
    konto_type2 = models.CharField(max_length=1, choices=konto_types2, default='-')
    konto_type3 = models.CharField(max_length=3, choices=konto_types3)
    def __unicode__(self):
        return self.konto_title


class Buchung(models.Model):
    buchung_descr = models.CharField('Description', max_length=128)
    buchung_amount = models.FloatField(default=0)
    buchung_sollKonto = models.ForeignKey(Konto, related_name='sollKonto')
    buchung_habenKonto = models.ForeignKey(Konto, related_name='habenKonto')
    buchung_date = models.DateField('Buchungsdatum')
    buchung_tags = TaggableManager(blank=True)
    buchung_user = models.ForeignKey(User)
    def __unicode__(self):
        return self.buchung_descr