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
                'recommend': parameter.recommend,
                'delete_form': DeleteParameterForm(initial={'action': 'delete', 'pk': parameter.id})
            }
            items.append(item)
        return items
        
    def get(self, request):
        parameters = self.get_parameters()
        items = self.get_items(parameters)

        context = {
            'items': items, 
            'search_parameter_form': SearchParameterForm(initial={'action': 'search_parameter'})
        }
        return TemplateResponse(request, self.template_name, context)

    def search_parameter(self, request):
        form = SearchParameterForm(request.POST)
        if form.is_valid():
            items = self.get_parameter_from_form(form)

            if items:
                context = {
                    'search_parameter_form': SearchParameterForm(initial={'action': 'search_parameter'}),
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


    def delete_parameter(self, request):
        form = DeleteParameterForm(request.POST)
        if form.is_valid():
            form.save()
            parameters = self.get_parameters()
            items = self.get_items(parameters)

            context = {
                'items': items, 
                'search_parameter_form': form, 
                'success': 'Deleted'
            }
            return TemplateResponse(request, self.template_name, context)

        parameters = self.get_parameters()
        items = self.get_items(parameters)

        context = {
            'items': items, 
            'search_parameter_form': form, 
        }
        return TemplateResponse(request, self.template_name, context)


    def post(self, request):
        action = request.POST['action']     
        if action == 'search_parameter':
            return self.search_parameter(request)
        elif action == 'delete':
            return self.delete_parameter(request)
        else:
            parameters = self.get_parameters()
            items = self.get_items(parameters)
            context = {'items': items, 'error': 'Unknown action'}
            return TemplateResponse(request, self.template_name, context)

