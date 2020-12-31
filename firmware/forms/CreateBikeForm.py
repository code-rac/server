import re
from django import forms
from django.core.exceptions import ValidationError

from ..models import Bike

class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats = ('%d-%m-%Y')
    
class CreateBikeForm(forms.Form):

    name = forms.CharField()
    ecu_id = forms.CharField()
    generation = forms.IntegerField()
    code = forms.CharField()
    start_at = forms.DateField(widget=DateInput)
    is_used = forms.BooleanField()
    cc = forms.IntegerField()

    def clean_ecu_id(self):
        ecu_id = self.cleaned_data['ecu_id']
        if not re.search(r'\S{2}-\S{2}-\S{2}-\S{2}', ecu_id):
            raise ValidationError('{} must have the format XX-XX-XX-XX'.format(ecu_id))
        return ecu_id

    def save(self):
        bike = Bike.objects.create(**self.cleaned_data)
        bike.save()
