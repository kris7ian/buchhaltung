from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field

from bilanz import models


class AddBuchungForm(forms.ModelForm):
    class Meta:
        fields = ('buchung_descr','buchung_amount', 'buchung_sollKonto', 'buchung_habenKonto', 'buchung_date', 'buchung_tags',)
        model = models.Buchung




class AddKontoForm(forms.ModelForm):
    class Meta:
        fields = ('konto_title','konto_erfolgswirksam', 'konto_type', 'konto_type2', 'konto_type3',)
        model = models.Konto

    def __init__(self, *args, **kwargs):
        super(AddKontoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'konto_title',
            'konto_erfolgswirksam',
            'konto_type',
            'konto_type2',
            ButtonHolder(
                Submit('neues-konto', 'Create', css_class='btn-primary')
            )
        )