from django import template
from django.db.models import Sum
from bilanz.models import Buchung

register = template.Library()

def kontoSum(konto_id, konto_type):
    '''Description...'''

    if konto_type == 'A':
        plus = Buchung.objects.filter(buchung_sollKonto=konto_id).aggregate(Sum('buchung_amount'))
        minus = Buchung.objects.filter(buchung_habenKonto=konto_id).aggregate(Sum('buchung_amount'))

        if plus['buchung_amount__sum'] == None:
            plus['buchung_amount__sum'] = 0
        if minus['buchung_amount__sum'] == None:
            minus['buchung_amount__sum'] = 0
        return plus['buchung_amount__sum'] - minus['buchung_amount__sum']
    else:
        plus = Buchung.objects.filter(buchung_habenKonto=konto_id).aggregate(Sum('buchung_amount'))
        minus = Buchung.objects.filter(buchung_sollKonto=konto_id).aggregate(Sum('buchung_amount'))

        if plus['buchung_amount__sum'] == None:
            plus['buchung_amount__sum'] = 0
        if minus['buchung_amount__sum'] == None:
            minus['buchung_amount__sum'] = 0
        return plus['buchung_amount__sum'] - minus['buchung_amount__sum']

register.simple_tag(kontoSum)
