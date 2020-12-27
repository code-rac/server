from django import forms

class FirmwareSearchForm(forms.Form):

    name = forms.CharField()
    json = forms.BooleanField(required=False)

    # class Meta:
    #     model = Firmware
    #     fields = ('name',)