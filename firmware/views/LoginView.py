from django.views import View
from django.contrib.auth import login
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm

class LoginView(View):
    template_name = 'firmware/login.html'

    def get(self, request):
        context = {'form': AuthenticationForm(request)}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')

        context = {'form': form}
        return TemplateResponse(request, self.template_name, context)
