from ..models import *
from django import forms
from ..models import User

class ReadWriteForm(forms.Form):

    CHOICES = [
        ('None', 'None'), 
        ('Read', 'Read'),
        ('Write', 'Write'), 
        ('Read/Write', 'Read/Write')
    ]

    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    username = forms.CharField(widget=forms.HiddenInput)

    def save(self):
        choice = self.cleaned_data['choice']
        user = User.objects.get(username=self.data['username'])

        if choice == 'None':
            user.readable = False
            user.writable = False
        elif choice == 'Read':
            user.readable = True
            user.writable = False
        elif choice == 'Write':
            user.readable = False
            user.writable = True
        elif choice == 'Read/Write':
            user.readable = True
            user.writable = True
        else:
            raise NotImplementedError

        user.save()