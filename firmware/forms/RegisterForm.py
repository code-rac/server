from ..models import *
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': ('The two password fields didn\'t match.'),
    }
    password1 = forms.CharField(label=('Password'),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=('Password confirmation'),
        widget=forms.PasswordInput,
        help_text=('Enter the same password as above, for verification.'))    
    code = forms.CharField()

    class Meta:
        model = User
        fields = ('username',)    

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


    def clean_code(self):
        code = self.cleaned_data['code']
        if not Code.objects.filter(name=code).exists():
            raise ValidationError('Code did not exist')
        if Code.objects.get(name=code).is_used:
            raise ValidationError('Code is used')
        return code


    def save(self, commit=True):
        code = Code.objects.get(name=self.cleaned_data['code'])
        code.is_used = True
        code.save()

        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user