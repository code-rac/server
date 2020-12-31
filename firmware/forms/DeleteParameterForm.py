from django import forms
from django.core.exceptions import ValidationError

from ..models import *

class DeleteParameterForm(forms.Form):

    pk = forms.IntegerField(widget=forms.HiddenInput)
    action = forms.CharField(widget=forms.HiddenInput)

    def save(self):
        pk = self.cleaned_data['pk']
        for bp in BikeParameter.objects.filter(parameter_id=pk).all():
            bp.delete()

        for bpe in BikeParameterExpression.objects.filter(parameter_id=pk).all():
            bpe.delete()
        obj = Parameter.objects.get(pk=pk)
        obj.delete()
        