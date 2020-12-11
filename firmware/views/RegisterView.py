from ..forms import *
from django.views import View
from django.template.response import TemplateResponse


class RegisterView(View):

    template_name = 'firmware/register.html'

    def get(self, request):
        context = {'form': RegisterForm()}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(data=request.POST)        
        if form.is_valid():
            form.save()
            context = {'form': form, 'success': 'Registered'}
            return TemplateResponse(request, self.template_name, context)        

        context = {'form': form}
        return TemplateResponse(request, self.template_name, context)