from django import template
from django.db.models import Sum
from bilanz.models import Buchung

register = template.Library()

def kontoSum(konto_id, konto_type):
    '''Description...'''

    if konto_type == 'A':
        plus = Buchung.objects.filter(buchung_sollKonto=konto_id)
        minus = Buchung.objects.filter(buchung_habenKonto=konto_id)

        plus_amount = 0
        minus_amount = 0

        for buchung in plus:
            if buchung.buchung_rate != 1:
                plus_amount += buchung.buchung_amount * buchung.buchung_rate
            else:
                plus_amount += buchung.buchung_amount

        for buchung in minus:
            if buchung.buchung_rate != 1:
                minus_amount += buchung.buchung_amount * buchung.buchung_rate
            else:
                minus_amount += buchung.buchung_amount


        return int((plus_amount - minus_amount) * 100) / 100


    else:
        plus = Buchung.objects.filter(buchung_habenKonto=konto_id)
        minus = Buchung.objects.filter(buchung_sollKonto=konto_id)

        minus_amount = 0
        plus_amount = 0

        for buchung in minus:
            if buchung.buchung_rate != 1:
                minus_amount += buchung.buchung_amount * buchung.buchung_rate
            else:
                minus_amount += buchung.buchung_amount

        for buchung in plus:
            if buchung.buchung_rate != 1:
                plus_amount += buchung.buchung_amount * buchung.buchung_rate
            else:
                plus_amount += buchung.buchung_amount

        return int((plus_amount - minus_amount) * 100) / 100


register.simple_tag(kontoSum)
