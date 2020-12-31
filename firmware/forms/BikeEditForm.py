from django import forms
from django.core.exceptions import ValidationError

from ..models import Bike

class BikeEditForm(forms.Form):

    name = forms.CharField()
    ecu_id = forms.CharField()
    generation = forms.IntegerField()
    code = forms.CharField()
    start_at = forms.DateField()
    is_used = forms.BooleanField()
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
