from django import forms
from ..models import Firmware

class FirmwareSearchForm(forms.Form):

    name = forms.CharField()
    json = forms.BooleanField(required=False)

    # class Meta:
    #     model = Firmware
    #     fields = ('name',)