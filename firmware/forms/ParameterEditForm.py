from ..models import *
from django import forms
from django.core.exceptions import ValidationError

class ParameterEditForm(forms.Form):
    
    pk = forms.IntegerField(widget=forms.HiddenInput)

    name = forms.CharField()
    name_vn = forms.CharField()
    description = forms.CharField()
    unit = forms.CharField()
    upper = forms.FloatField()
    lower = forms.FloatField()
    recommend = forms.FloatField()
    

    def save(self):
        user = Parameter.objects.get(pk=self.cleaned_data['pk'])
        user.__dict__.update(self.cleaned_data)
        user.save()

    
    def clean_recommend(self):
        lower = self.cleaned_data['lower']
        upper = self.cleaned_data['upper']
        recommend = self.cleaned_data['recommend']
        if recommend > upper or recommend < lower:
            raise ValidationError('Recommend {} must less than Upper {} or more than Lower {}.'.format(recommend, upper, lower))
        return recommend
