from django import forms
from django.core.exceptions import ValidationError

from ..models import Firmware
from ..models import Code

class CreateFirmwareForm(forms.Form):

    name = forms.CharField()
    offset = forms.CharField()
    file = forms.FileField()
    # code = forms.CharField()

    # class Meta:
    #     model = Firmware
    #     fields = ('name', 'offset', 'file')

    # def clean_code(self):
    #     code = self.cleaned_data['code']
    #     if not Code.objects.filter(name=code).exists():
    #         raise ValidationError('Code did not exist')
    #     else:
    #         code = Code.objects.get(name=code)
    #     print(type(code))
    #     return code

    def save(self):
        firmware = Firmware.objects.create(**self.cleaned_data)
        firmware.save()
        return firmware