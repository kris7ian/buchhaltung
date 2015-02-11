from django.db import models
# from taggit.managers import TaggableManager

# class Tag(models.Model):
#    tag_tag = models.CharField('Tag', max_length=80)
#    def __str__(self):
#        return self.tag_tag

class Konto(models.Model):
    konto_title = models.CharField(max_length=200)
    konto_anfangsBestand = models.IntegerField(default=0)
    konto_sum = models.IntegerField(default=0)
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
    konto_type = models.CharField(max_length=1, choices=konto_types)
    konto_type2 = models.CharField(max_length=1, choices=konto_types2, default='-')
    def __str__(self):
        return self.konto_title


class Buchung(models.Model):
    buchung_descr = models.CharField('Description', max_length=128)
    buchung_amount = models.IntegerField(default=0)
    buchung_sollKonto = models.ForeignKey(Konto, related_name='sollKonto')
    buchung_habenKonto = models.ForeignKey(Konto, related_name='habenKonto')
    buchung_date = models.DateField('Buchungsdatum')
    #buchung_tags = TaggableManager(blank=True)
    def __str__(self):
        return self.buchung_descr