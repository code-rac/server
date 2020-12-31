from django import forms
from ..models import *

class SelectParameterForm(forms.Form):
    try:
        CHOICES = tuple([['-', '-']] + [[bp.id, bp.name] for bp in Parameter.objects.all()])
    except:
        CHOICES = tuple([['-', '-']])

    choice = forms.ChoiceField(label='', choices=CHOICES, widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))
    row = forms.IntegerField(widget=forms.HiddenInput)
    column = forms.IntegerField(widget=forms.HiddenInput)
    action = forms.CharField(widget=forms.HiddenInput)
    is_used = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onchange': 'this.form.submit();'}))

    def get_bp_name(self, parameter_id, row, column):
        p = Parameter.objects.get(pk=parameter_id)
        return '{}_{}_{}'.format(p.name, row, column)

    def get_bpe_name(self, bike_id, parameter_id):
        bps = BikeParameter.objects.filter(parameter_id=parameter_id, bike_id=bike_id).all()
        return '+'.join(bp.name for bp in bps)

    def save(self, bike_id):
        parameter_id = self.cleaned_data['choice']
        row = self.cleaned_data['row']
        column = self.cleaned_data['column']
        is_used = self.cleaned_data['is_used']

        try:
            old_bp = BikeParameter.objects.get(bike_id=bike_id, row=row, column=column)
        except BikeParameter.DoesNotExist:
            if parameter_id != '-':
                bp = BikeParameter.objects.create(
                    bike_id=bike_id, 
                    parameter_id=parameter_id, 
                    row=row, 
                    column=column, 
                    name=self.get_bp_name(parameter_id, row, column)
                )
                try:
                    bpe = BikeParameterExpression.objects.get(bike_id=bike_id, parameter_id=parameter_id)
                except BikeParameterExpression.DoesNotExist:
                    bpe = BikeParameterExpression.objects.create(
                        bike_id=bike_id, 
                        parameter_id=parameter_id, 
                        expression=self.get_bpe_name(bike_id, parameter_id)
                    )
        else:
            old_parameter_id = old_bp.parameter_id
            if parameter_id != '-':
                old_bp.parameter_id = parameter_id
                old_bp.name = self.get_bp_name(parameter_id, row, column)
                old_bp.save()
                bps = BikeParameter.objects.filter(bike_id=bike_id, parameter_id=old_parameter_id).all()
                if len(bps) == 0:
                    bpe = BikeParameterExpression.objects.get(bike_id=bike_id, parameter_id=old_parameter_id)
                    bpe.delete()
                try:
                    bpe = BikeParameterExpression.objects.get(bike_id=bike_id, parameter_id=parameter_id)
                except BikeParameterExpression.DoesNotExist:
                    bpe = BikeParameterExpression.objects.create(
                        bike_id=bike_id, 
                        parameter_id=parameter_id, 
                        expression=self.get_bpe_name(bike_id, parameter_id)
                    )
            else:
                old_bp.delete()
                bps = BikeParameter.objects.filter(bike_id=bike_id, parameter_id=old_bp.parameter_id).all()
                if len(bps) == 0:
                    bpe = BikeParameterExpression.objects.get(bike_id=bike_id, parameter_id=old_parameter_id)
                    bpe.delete()

        if parameter_id != '-':
            bp = BikeParameter.objects.get(bike_id=bike_id, row=row, column=column)
            bp.is_used = is_used
            bp.save()
