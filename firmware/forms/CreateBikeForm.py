from django import forms
from django.core.exceptions import ValidationError

from ..models import Bike

class CreateBikeForm(forms.ModelForm):

    class Meta:
        model = Bike
        fields = ('name', )
