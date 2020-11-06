from django import forms
from ..models import Firmware

class FirmwareSearchForm(forms.ModelForm):

    class Meta:
        model = Firmware
        fields = ('name',)