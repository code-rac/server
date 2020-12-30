from django import forms
from django.core.exceptions import ValidationError

from ..models import Parameter

class CreateParameterForm(forms.ModelForm):

    class Meta:
        model = Parameter
        fields = ('name', 'name_vn', 'description', 'unit', 'upper', 'lower', 'recommend')

    def clean_recommend(self):
        lower = self.cleaned_data['lower']
        upper = self.cleaned_data['upper']
        recommend = self.cleaned_data['recommend']
        if recommend > upper or recommend < lower:
            raise ValidationError('Recommend {} must less than Upper {} or more than Lower {}.'.format(recommend, upper, lower))
        return recommend
