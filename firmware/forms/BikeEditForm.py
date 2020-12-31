import re
from django import forms
from django.core.exceptions import ValidationError

from ..models import Bike

class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats = ('%d-%m-%Y')

class BikeEditForm(forms.Form):

    name = forms.CharField()
    ecu_id = forms.CharField()
    generation = forms.IntegerField()
    code = forms.CharField()
    # start_at = forms.DateField(widget=forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}))
    start_at = forms.DateField(widget=DateInput)
    is_used = forms.BooleanField(label='', required=False, widget=forms.CheckboxInput(attrs={'onchange': 'this.form.submit();'}))
    cc = forms.IntegerField()
    action = forms.CharField(widget=forms.HiddenInput)
    pk = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        bike = Bike.objects.get(pk=self.cleaned_data['pk'])
        bike.name = self.cleaned_data['name']
        bike.ecu_id = self.cleaned_data['ecu_id']
        bike.generation = self.cleaned_data['generation']
        bike.code = self.cleaned_data['code']
        bike.start_at = self.cleaned_data['start_at']
        bike.is_used = self.cleaned_data['is_used']
        bike.cc = self.cleaned_data['cc']
        bike.save()

    def clean_ecu_id(self):
        ecu_id = self.cleaned_data['ecu_id']
        if not re.search(r'\S{2}-\S{2}-\S{2}-\S{2}', ecu_id):
            raise ValidationError('{} must have the format XX-XX-XX-XX'.format(ecu_id))
        return ecu_id