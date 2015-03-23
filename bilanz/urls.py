from django.conf.urls import patterns, url

from bilanz import views

urlpatterns = patterns('',
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^bilanz/', views.BilanzView.as_view(), name='bilanz'),
    url(r'^buchungen/', views.BuchungenView.as_view(), name='buchungen'),
    url(r'^erfolgsrechnung/', views.ErfolgsrechnungView.as_view(), name='erfolgsrechnung'),
    url(r'^neue-buchung/', views.AddBuchungView.as_view(), name='add-buchung'),
    url(r'^hinzufuegen/buchung/(?P<pk>\d+)', views.CopyBuchungView.as_view(), name='copy-buchung'),
    url(r'^hinzufuegen/buchung/', views.AddBuchungView2.as_view(), name='add-buchung2'),
    url(r'^hinzufuegen/konto/', views.AddKontoView2.as_view(), name='add-konto2'),
    url(r'^aendern/konto/(?P<pk>\d+)', views.EditKontoView.as_view(), name='edit-konto'),
    url(r'^aendern/buchung/(?P<pk>\d+)', views.EditBuchungView.as_view(), name='edit-buchung'),
    url(r'^konto/(?P<pk>\d+)', views.DetailKontoView.as_view(), name='detail-konto'),
    url(r'^neues-konto/', views.AddKontoView.as_view(), name='add-konto'),
)