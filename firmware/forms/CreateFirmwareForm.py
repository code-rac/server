from django import forms
from django.core.exceptions import ValidationError

from ..models import Firmware
from ..models import Code

class CreateFirmwareForm(forms.Form):

    name = forms.CharField()
    offset = forms.CharField()
    file = forms.FileField()
    
    def save(self):
        firmware = Firmware.objects.create(**self.cleaned_data)
        firmware.save()
