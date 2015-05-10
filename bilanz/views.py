from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.db.models import Sum

from django.views import generic

from braces.views import LoginRequiredMixin

from bilanz.models import Konto
from bilanz.models import Buchung

from bilanz import forms

from bilanz.templatetags.gewinnVerlust import gewinnVerlust


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

    def get_context_data(self, **kwargs):
        context = super(BilanzView, self).get_context_data(**kwargs)
        context['gewinn'] = gewinnVerlust()
        return context


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bilanz/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['list'] = Buchung.objects.filter(buchung_date__month='2', buchung_sollKonto=1).values_list('buchung_sollKonto').annotate(total_amount=Sum('buchung_amount'))
        #print(context['list'][1])
        return context


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


class AddBuchungView2(LoginRequiredMixin, generic.FormView):
    template_name = 'bilanz/add_buchung2.html'

    form_class = forms.AddBuchungForm
    model = Buchung

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.buchung_user = self.request.user
        self.object.save()
        #self.object.buchung_tags.add("red", "green", "fruit")
        form.save_m2m()


        return super(AddBuchungView2, self).form_valid(form)

    def get_success_url(self):
        return reverse('buchungen')


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


class AddKontoView2(LoginRequiredMixin, generic.CreateView):
    template_name = 'bilanz/add_konto.html'

    form_class = forms.AddKontoForm
    model = Konto

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.user = self.request.user
        self.object.save()
        return super(AddKontoView2, self).form_valid(form)

    def get_success_url(self):
        return reverse('bilanz')


class EditKontoView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'bilanz/edit_konto.html'

    form_class = forms.AddKontoForm
    model = Konto

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(EditKontoView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditKontoView, self).get_context_data(**kwargs)
        context['konto_details'] = self.get_object()
        return context

    def get_success_url(self):
        return reverse('bilanz')


class EditBuchungView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'bilanz/edit_buchung.html'

    form_class = forms.AddBuchungForm
    model = Buchung

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.buchung_user = self.request.user
        self.object.save()
        #self.object.buchung_tags.add("red", "green", "fruit")
        form.save_m2m()


        return super(EditBuchungView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditBuchungView, self).get_context_data(**kwargs)
        context['buchung_details'] = self.get_object()
        return context

    def get_success_url(self):
        return reverse('buchungen')


class CopyBuchungView(LoginRequiredMixin, generic.CreateView):
    template_name = 'bilanz/edit_buchung.html'

    form_class = forms.AddBuchungForm
    model = Buchung

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.buchung_user = self.request.user
        self.object.save()
        #self.object.buchung_tags.add("red", "green", "fruit")
        form.save_m2m()


        return super(CopyBuchungView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CopyBuchungView, self).get_context_data(**kwargs)
        context['buchung_details'] = self.get_object()
        context['copy_view'] = True
        return context

    def get_success_url(self):
        return reverse('buchungen')


class DeleteBuchungView(LoginRequiredMixin, generic.DeleteView):
    model = Buchung

    def get_success_url(self):
        return reverse('buchungen')


class DetailKontoView(LoginRequiredMixin, generic.ListView):
    template_name='bilanz/konto.html'
    context_object_name = 'buchungen_sollList'

    def get_queryset(self):
        '''Get all Buchungen.'''
        if Buchung.objects.filter(buchung_sollKonto = self.kwargs['pk']).order_by('-buchung_date') != True:
            return Buchung.objects.filter(buchung_sollKonto = self.kwargs['pk']).order_by('-buchung_date')
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super(DetailKontoView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['pk']
        context['buchungen_habenList'] = Buchung.objects.filter(buchung_habenKonto = self.kwargs['pk']).order_by('-buchung_date')
        context['konto'] = Konto.objects.get(id=self.kwargs['pk'])
        return context
