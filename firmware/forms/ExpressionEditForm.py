from django import forms
from ..models import *

class ExpressionEditForm(forms.Form):

    bike_id = forms.IntegerField(widget=forms.HiddenInput)
    parameter_id = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name_vn = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    expression = forms.CharField()

    action = forms.CharField(widget=forms.HiddenInput)

    def save(self):
        bike_id = self.cleaned_data['bike_id']
        parameter_id = self.cleaned_data['parameter_id']
        expression = self.cleaned_data['expression']
        bp = BikeParameter.objects.get(bike_id=bike_id, parameter_id=parameter_id)
        bp.expression = expression
        bp.save()
