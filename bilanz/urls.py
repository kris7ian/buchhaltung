from django.conf.urls import patterns, url

from bilanz import views

urlpatterns = patterns('',
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^bilanz/', views.BilanzView.as_view(), name='bilanz'),
    url(r'^buchungen/', views.BuchungenView.as_view(), name='buchungen'),
    url(r'^erfolgsrechnung/', views.ErfolgsrechnungView.as_view(), name='erfolgsrechnung'),
    url(r'^neue-buchung/', views.AddBuchungView.as_view(), name='add-buchung'),
    url(r'^neues-konto/', views.AddKontoView.as_view(), name='add-konto'),
)