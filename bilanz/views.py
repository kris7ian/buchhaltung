from django.http import HttpResponse
from django.template import RequestContext, loader

from bilanz.models import Konto
from bilanz.models import Buchung

def index(request):
    bilanz_liste_aktiv = Konto.objects.filter(konto_type="A", konto_erfolgswirksam=False)
    bilanz_liste_passiv = Konto.objects.filter(konto_type="P", konto_erfolgswirksam=False)
    erfolg_liste_aufwand = Konto.objects.filter(konto_type="A", konto_erfolgswirksam=True)
    erfolg_liste_ertrag = Konto.objects.filter(konto_type="P", konto_erfolgswirksam=True)
    buchungen = Buchung.objects.all().order_by('-buchung_date')
    
    template = loader.get_template('bilanz/index.html')
    context = RequestContext(request, {
        'bilanz_liste_aktiv': bilanz_liste_aktiv,
        'bilanz_liste_passiv': bilanz_liste_passiv,
        'erfolg_liste_aufwand': erfolg_liste_aufwand,
        'erfolg_liste_ertrag': erfolg_liste_ertrag,
        'buchungen' : buchungen,
    })
    return HttpResponse(template.render(context))