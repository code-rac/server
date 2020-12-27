from django import forms

class SearchUserForm(forms.Form):

    code = forms.CharField(required=False)
    phone = forms.CharField(required=False)

