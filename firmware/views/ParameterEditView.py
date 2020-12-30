from django.views import View
from django.template.response import TemplateResponse

from ..models import *
from ..forms import *

class ParameterEditView(View):

    template_name = 'firmware/parameter.html'

    def get_parameter(self, pk):
        parameter = Parameter.objects.get(pk=pk)
        initial = {
            'pk': parameter.pk,
            'name': parameter.name,
            'name_vn': parameter.name_vn, 
            'description': parameter.description, 
            'unit': parameter.unit, 
            'upper': parameter.upper, 
            'lower': parameter.lower, 
            'recommend': parameter.recommend
        }
        form = ParameterEditForm(initial=initial)
        return form

    def get(self, request, pk):
        form = self.get_parameter(pk)
        context = {'parameter_edit_form': form}
        return TemplateResponse(request, self.template_name, context)


    def post(self, request, pk):
        form = ParameterEditForm(data=request.POST)        
        if form.is_valid():
            form.save()
            context = {'success': 'Changed', 'parameter_edit_form': form}
            return TemplateResponse(request, self.template_name, context)        

        context = {'parameter_edit_form': form}
        return TemplateResponse(request, self.template_name, context)


