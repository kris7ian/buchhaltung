from django import template
from django.db.models import Sum
from bilanz.models import Buchung
from yahoo_finance import Currency

register = template.Library()

def kontoSumForeignCurrency(konto_id, konto_type, konto_currency):
    '''Description...'''

    currencyCode = 'CHF' + konto_currency
    currencyRate = Currency(currencyCode)

    if konto_type == 'A':
        plus = Buchung.objects.filter(buchung_sollKonto=konto_id)
        minus = Buchung.objects.filter(buchung_habenKonto=konto_id).aggregate(Sum('buchung_amount'))

        plus_amount = 0

        for buchung in plus:
            if buchung.buchung_rate != 1:
                plus_amount += buchung.buchung_amount * buchung.buchung_rate
            else:
                plus_amount += buchung.buchung_amount

        if minus['buchung_amount__sum'] == None:
            minus['buchung_amount__sum'] = 0

        amount = float(plus_amount - minus['buchung_amount__sum'])

        convertedAmount = amount * 1/float(currencyRate.get_bid())

        return int(convertedAmount * 100) / 100

    else:
        plus = Buchung.objects.filter(buchung_habenKonto=konto_id).aggregate(Sum('buchung_amount'))
        minus = Buchung.objects.filter(buchung_sollKonto=konto_id)

        minus_amount = 0

        for buchung in minus:
            if buchung.buchung_rate != 1:
                minus_amount += buchung.buchung_amount * buchung.buchung_rate
            else:
                minus_amount += buchung.buchung_amount

        if plus['buchung_amount__sum'] == None:
            plus['buchung_amount__sum'] = 0

        amount = float(plus['buchung_amount__sum'] - minus_amount)
        convertedAmount = amount * 1/float(currencyRate.get_bid())

        return int(convertedAmount * 100) / 100


register.simple_tag(kontoSumForeignCurrency)
