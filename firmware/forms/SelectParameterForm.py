from django import forms
from ..models import *

class SelectParameterForm(forms.Form):

    CHOICES = tuple([['-', '-']] + [[item.id, item.name] for item in Parameter.objects.all()])

    choice = forms.ChoiceField(label='', choices=CHOICES, widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))
    row = forms.IntegerField(widget=forms.HiddenInput)
    column = forms.IntegerField(widget=forms.HiddenInput)

    def save(self, bike_id):
        '''# kich ban:
        - TH1: bike_id chua noi voi parameter_id:
            => create
        - TH2: bike_id da noi voi parameter_id:
            a) noi sang cai khac:
                => update
            b) noi sang None:
                => delete
        '''
        parameter_id = self.cleaned_data['choice']
        row = self.cleaned_data['row']
        column = self.cleaned_data['column']

        try:
            item = BikeParameter.objects.get(bike_id=bike_id, row=row, column=column)
                    
        except BikeParameter.DoesNotExist:
            if parameter_id != '-':
                item = BikeParameter.objects.create(bike_id=bike_id, parameter_id=parameter_id, row=row, column=column)

        else:
            if parameter_id != '-':
                item.parameter_id = parameter_id
                item.save()
            else:
                item.delete()