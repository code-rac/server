from django import forms
from django.core.exceptions import ValidationError

from ..models import *

class DeleteBikeForm(forms.Form):

    pk = forms.IntegerField(widget=forms.HiddenInput)
    action = forms.CharField(widget=forms.HiddenInput)

    def save(self):
        pk = self.cleaned_data['pk']
        for bp in BikeParameter.objects.filter(bike_id=pk).all():
            bp.delete()

        for bpe in BikeParameterExpression.objects.filter(bike_id=pk).all():
            bpe.delete()
        obj = Bike.objects.get(pk=pk)
        obj.delete()
        