from django.contrib import admin
from bilanz.models import Konto
from bilanz.models import Buchung



class KontoAdmin(admin.ModelAdmin):

    # define which Konto columns to show in the admin
    list_display = ('konto_title', 'konto_type', 'id', 'konto_erfolgswirksam')



class BuchungAdmin(admin.ModelAdmin):

    # define which Buchung columns to show in the admin
    list_display = ('buchung_descr', 'buchung_amount', 'buchung_date')

    #readonly_fields = ('buchung_sollKonto', 'buchung_habenKonto')


admin.site.register(Konto, KontoAdmin)
admin.site.register(Buchung, BuchungAdmin)
