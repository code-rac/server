from django import forms
from ..models import *

class ExpressionEditForm(forms.Form):

    bike_id = forms.IntegerField(widget=forms.HiddenInput)
    parameter_id = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name_vn = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    variable_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    expression = forms.CharField()
    action = forms.CharField(widget=forms.HiddenInput)
    is_used = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onchange': 'this.form.submit();'}))

    def save(self):
        bike_id = self.cleaned_data['bike_id']
        parameter_id = self.cleaned_data['parameter_id']
        expression = self.cleaned_data['expression']
        is_used = self.cleaned_data['is_used']
        bpe = BikeParameterExpression.objects.get(bike_id=bike_id, parameter_id=parameter_id)
        bpe.expression = expression
        bpe.is_used = is_used
        bpe.save()
