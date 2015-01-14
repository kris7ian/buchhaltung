from django.contrib import admin
from bilanz.models import Konto
from bilanz.models import Buchung



class KontoAdmin(admin.ModelAdmin):

    # define which Konto columns to show in the admin
    list_display = ('konto_title', 'konto_type', 'konto_anfangsBestand', 'konto_sum', 'konto_id', 'konto_erfolgswirksam')



class BuchungAdmin(admin.ModelAdmin):

    # define which Buchung columns to show in the admin
    list_display = ('buchung_descr', 'buchung_amount', 'buchung_date')

    #readonly_fields = ('buchung_sollKonto', 'buchung_habenKonto')

    # define the save model
    def save_model(self, request, obj, form, change):
        # buchung is the initial value and obj the changed value

        # check if Buchung was added or changed
        if change == True:

            # get the objects
            buchung = Buchung.objects.get(buchung_id = obj.buchung_id)

            print('buchung.buchung_descr: ' + buchung.buchung_descr )
            print('obj.buchung_descr: ' + obj.buchung_descr )

            # calculate the change of the buchung_amount
            amountChange = obj.buchung_amount - buchung.buchung_amount

            # check if sollKonto has changed
            if obj.buchung_sollKonto_id != buchung.buchung_sollKonto_id:

                # check which type the initial konto is and reverse the buchung
                sollKonto_initial = Konto.objects.get(konto_id = buchung.buchung_sollKonto_id)

                if sollKonto_initial.konto_type == 'A':
                    sollKonto_initial.konto_sum = sollKonto_initial.konto_sum - buchung.buchung_amount
                else:
                    sollKonto_initial.konto_sum = sollKonto_initial.konto_sum + buchung.buchung_amount

                # save the object
                sollKonto_initial.save()

                # check which type the new konto is and do the buchung
                sollKonto = Konto.objects.get(konto_id = obj.buchung_sollKonto_id)
                if sollKonto.konto_type == 'A':
                    sollKonto.konto_sum = sollKonto.konto_sum + obj.buchung_amount
                else:
                    sollKonto.konto_sum = sollKonto.konto_sum - obj.buchung_amount

                # save the object
                sollKonto.save()


            # check if habenKonto has changed
            if obj.buchung_habenKonto_id != buchung.buchung_habenKonto_id:

                # check which type the initial konto is and reverse the buchung
                habenKonto_initial = Konto.objects.get(konto_id = buchung.buchung_habenKonto_id)

                if habenKonto_initial.konto_type == 'P':
                    habenKonto_initial.konto_sum = habenKonto_initial.konto_sum - buchung.buchung_amount
                else:
                    habenKonto_initial.konto_sum = habenKonto_initial.konto_sum + buchung.buchung_amount

                # save the object
                # !!! this line below is what doesn't seem to work !!!
                habenKonto_initial.save()

                # check which type the new konto is and do the buchung
                habenKonto = Konto.objects.get(konto_id = obj.buchung_habenKonto_id)
                if habenKonto.konto_type == 'P':
                    habenKonto.konto_sum = habenKonto.konto_sum + obj.buchung_amount
                else:
                    habenKonto.konto_sum = habenKonto.konto_sum - obj.buchung_amount

                # save the object
                habenKonto.save()

            # check if buchung_amount has changed
            if amountChange != 0:
                if obj.buchung_sollKonto_id == buchung.buchung_sollKonto_id:
                    sollKonto = Konto.objects.get(konto_id = obj.buchung_sollKonto_id)
                    if sollKonto.konto_type == 'A':
                        sollKonto.konto_sum = sollKonto.konto_sum + amountChange
                    else:
                        sollKonto.konto_sum = sollKonto.konto_sum - amountChange
                    # save the object
                    sollKonto.save()
                if obj.buchung_habenKonto_id == buchung.buchung_habenKonto_id:
                    habenKonto = Konto.objects.get(konto_id = obj.buchung_habenKonto_id)
                    if habenKonto.konto_type == 'P':
                        habenKonto.konto_sum = habenKonto.konto_sum + amountChange
                    else:
                        habenKonto.konto_sum = habenKonto.konto_sum - amountChange
                    # save the object
                    habenKonto.save()



        # no change, new one added
        else:
            sollKonto = Konto.objects.get(konto_id = obj.buchung_sollKonto_id)
            habenKonto = Konto.objects.get(konto_id = obj.buchung_habenKonto_id)
            if sollKonto.konto_type == 'A':
                sollKonto.konto_sum = sollKonto.konto_sum + obj.buchung_amount
            else:
                sollKonto.konto_sum = sollKonto.konto_sum - obj.buchung_amount
            if habenKonto.konto_type == 'P':
                habenKonto.konto_sum = habenKonto.konto_sum + obj.buchung_amount
            else:
                habenKonto.konto_sum = habenKonto.konto_sum - obj.buchung_amount
            sollKonto.save()
            habenKonto.save()

        # save the objects
        obj.save()



    # define the delete model
    def delete_model(self, request, obj):
        sollKonto = Konto.objects.get(konto_id = obj.buchung_sollKonto_id)
        habenKonto = Konto.objects.get(konto_id = obj.buchung_habenKonto_id)
        if sollKonto.konto_type == 'A':
            sollKonto.konto_sum = sollKonto.konto_sum - obj.buchung_amount
        else:
            sollKonto.konto_sum = sollKonto.konto_sum + obj.buchung_amount
        if habenKonto.konto_type == 'P':
            habenKonto.konto_sum = habenKonto.konto_sum - obj.buchung_amount
        else:
            habenKonto.konto_sum = habenKonto.konto_sum + obj.buchung_amount
        sollKonto.save()
        habenKonto.save()
        obj.delete()



admin.site.register(Konto, KontoAdmin)
admin.site.register(Buchung, BuchungAdmin)
