from django import template
from bilanz.models import Konto
from bilanz.templatetags.kontoSum import kontoSum
from bilanz.templatetags.kontoSumForeignCurrency import kontoSumForeignCurrency

register = template.Library()

def totalSum(kontotype, kontoerfolgswirksam):
    if kontoerfolgswirksam == False:
        konten = Konto.objects.filter(konto_type=kontotype).filter(konto_erfolgswirksam=False)
        sum = 0

        for konto in konten:
            if konto.konto_currency != 'CHF':
                sum += kontoSumForeignCurrency(konto.id, konto.konto_type, konto.konto_currency)
            else:
                sum += kontoSum(konto.id, konto.konto_type)

        return sum
    else:
        konten = Konto.objects.filter(konto_type=kontotype).filter(konto_erfolgswirksam=True)
        sum = 0

        for konto in konten:
            sum += kontoSum(konto.id, konto.konto_type)

        return sum

register.simple_tag(totalSum)