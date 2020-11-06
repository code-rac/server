from django import forms
from ..models import Firmware

class CreateFirmwareForm(forms.ModelForm):

    class Meta:
        model = Firmware
        fields = ('name', 'offset', 'file')