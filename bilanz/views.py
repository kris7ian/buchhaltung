from django.http import HttpResponse
from django.template import RequestContext, loader

from bilanz.models import Konto
from bilanz.models import Buchung

def index(request):
    konten_liste_aktiv = Konto.objects.filter(konto_type="A")
    konten_liste_passiv = Konto.objects.filter(konto_type="P")
    buchungen = Buchung.objects.all()
    template = loader.get_template('bilanz/index.html')
    context = RequestContext(request, {
        'konten_liste_aktiv': konten_liste_aktiv,
        'konten_liste_passiv': konten_liste_passiv,
        'buchungen' : buchungen,
    })
    return HttpResponse(template.render(context))