from ..models import *
from django import forms

class UserEditForm(forms.Form):
    
    pk = forms.IntegerField(widget=forms.HiddenInput)
    username = forms.CharField()
    phone = forms.CharField()
    store_name = forms.CharField()
    address = forms.CharField()

    def save(self):
        user = User.objects.get(pk=self.cleaned_data['pk'])
        user.__dict__.update(self.cleaned_data)
        user.save()