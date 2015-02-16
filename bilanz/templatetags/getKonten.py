from django import template
from bilanz.models import Konto

register = template.Library()

@register.assignment_tag
def getKonten():
    return Konto.objects.all()
