from django import forms

class SearchParameterForm(forms.Form):

    name = forms.CharField(required=False)
    name_vn = forms.CharField(required=False)

