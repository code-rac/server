from django import forms
from ..models import *

class ExpressionEditForm(forms.Form):

    bike_id = forms.IntegerField(widget=forms.HiddenInput)
    parameter_id = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name_vn = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    expression = forms.CharField()

