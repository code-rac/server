from django import forms
from django.core.exceptions import ValidationError

from ..models import *

class BikeCloneForm(forms.Form):

    pk = forms.IntegerField(widget=forms.HiddenInput)
    action = forms.CharField(widget=forms.HiddenInput)

    def get_new_name(self, name):
        i = 0
        while True:
            i += 1
            new_name = name + '_clone_{}'.format(i)
            try:
                bike = Bike.objects.get(name=new_name)
            except Bike.DoesNotExist:
                break
        return new_name

    def save(self):
        pk = self.cleaned_data['pk']
        bike = Bike.objects.get(pk=pk)
        new_name = self.get_new_name(bike.name)
        new_bike = Bike.objects.create(
            name=new_name,
            generation=bike.generation,
            code=bike.code,
            start_at=bike.start_at,
            is_used=bike.is_used,
            cc=bike.cc
        )
        new_bike.save()

        bps = BikeParameter.objects.filter(bike_id=bike.id).all()
        for bp in bps:
            new_bp = BikeParameter.objects.create(
                name=bp.name,
                bike_id=new_bike.id,
                parameter_id=bp.parameter_id,
                row=bp.row,
                column=bp.column,
                is_used=bp.is_used
            )
            new_bp.save()

        bpes = BikeParameterExpression.objects.filter(bike_id=bike.id).all()
        for bpe in bpes:
            new_bpe = BikeParameterExpression.objects.create(
                bike_id=new_bike.id,
                parameter_id=bpe.parameter_id,
                expression=bpe.expression,
                is_used=bpe.is_used
            )
            new_bpe.save()



