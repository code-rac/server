from django.views import View
from django.template.response import TemplateResponse
from ..forms import *
from ..models import *
from . import util
from django.db.models import Q

class ParameterView(View):

    template_name = 'firmware/parameter.html'

    def get_parameters(self):
        parameters = Parameter.objects.all()
        return parameters

    def get_parameter_from_form(self, form):
        try:
            parameters = Parameter.objects.filter(
                Q(name__contains=form.cleaned_data['name']) & 
                Q(name_vn__contains=form.cleaned_data['name_vn']))
        except Parameter.DoesNotExist:
            parameters = []

        return self.get_items(parameters)


    def get_items(self, parameters):
        items = []
        for parameter in parameters:
            item = {
                'id': parameter.id,
                'name': parameter.name,
                'name_vn': parameter.name_vn, 
                'description': parameter.description, 
                'unit': parameter.unit, 
                'upper': parameter.upper, 
                'lower': parameter.lower, 
                'recommend': parameter.recommend
            }
            items.append(item)
        return items
        
    def get(self, request):
        parameters = self.get_parameters()
        items = self.get_items(parameters)
        context = {
            'items': items, 
            'search_parameter_form': SearchParameterForm()
        }
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = SearchParameterForm(request.POST)
        if form.is_valid():
            items = self.get_parameter_from_form(form)

            if items:
                context = {
                    'search_parameter_form': SearchParameterForm(),
                    'items': items
                }
            else:
                context = {
                    'search_parameter_form': form, 
                    'error': 'Parameter does not exist'
                }
        else:
            context = {
                'search_parameter_form': form,
            }
        return TemplateResponse(request, self.template_name, context)
