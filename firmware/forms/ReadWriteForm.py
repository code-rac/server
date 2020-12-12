from ..models import *
from django import forms


class ReadWriteForm(forms.Form):

    CHOICES = ['None', 'Read', 'Write', 'Read/Write']

    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)