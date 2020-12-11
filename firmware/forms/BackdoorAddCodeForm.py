from django import forms
from ..models import Code

class BackdoorAddCodeForm(forms.Form):

    name = forms.CharField()

    def save(self):
        code = Code.objects.create(**self.cleaned_data)
        code.save()
        return code

