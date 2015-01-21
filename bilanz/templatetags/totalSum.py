from django import template
from bilanz.models import Konto
from bilanz.templatetags.kontoSum import kontoSum

register = template.Library()

def totalSum(kontotype):
    konten = Konto.objects.filter(konto_type=kontotype).filter(konto_type2='-')
    sum = 0

    for konto in konten:
        sum += kontoSum(konto.konto_id, konto.konto_type)

    return sum

register.simple_tag(totalSum)