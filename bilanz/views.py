from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from django.views import generic

from braces.views import LoginRequiredMixin

from bilanz.models import Konto
from bilanz.models import Buchung

from bilanz import forms


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


class BuchungenView(LoginRequiredMixin, generic.ListView):
    template_name = 'bilanz/buchungen.html'
    context_object_name = 'buchung_list'

    def get_queryset(self):
        '''Get all Buchungen.'''
        if Buchung.objects.all().order_by('-buchung_date') != True:
            return Buchung.objects.all().order_by('-buchung_date')
        else:
            return False


class ErfolgsrechnungView(LoginRequiredMixin, generic.ListView):
    template_name = 'bilanz/erfolgsrechnung.html'
    context_object_name = 'erfolgskonto_list'

    def get_queryset(self):
        '''Get all Erfolgskonten.'''
        if Konto.objects.filter(konto_erfolgswirksam=True) != True:
            return Konto.objects.filter(konto_erfolgswirksam=True)
        else:
            return False

class BilanzView(LoginRequiredMixin, generic.ListView):
    template_name='bilanz/bilanz.html'
    context_object_name = 'bilanzkonto_list'

    def get_queryset(self):
        '''Get all Bilanzkonten.'''
        if Konto.objects.filter(konto_erfolgswirksam=False) != True:
            return Konto.objects.filter(konto_erfolgswirksam=False)
        else:
            return False


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bilanz/dashboard.html'


class AddBuchungView(LoginRequiredMixin, generic.CreateView):
    template_name = 'bilanz/add_buchung.html'

    form_class = forms.AddBuchungForm
    model = Buchung

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.user = self.request.user
        self.object.save()
        return super(AddBuchungView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bilanz')


class AddKontoView(LoginRequiredMixin, generic.CreateView):
    template_name = 'bilanz/add_buchung.html'

    form_class = forms.AddKontoForm
    model = Konto

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.user = self.request.user
        self.object.save()
        return super(AddKontoView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bilanz')