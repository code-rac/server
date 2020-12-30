from django.views import View
from django.template.response import TemplateResponse
from ..forms import CreateParameterForm

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator([csrf_exempt], name='dispatch')
class CreateParameterView(View):

    template_name = 'firmware/parameter.html'

    def get(self, request):
        context = {'create_parameter_form': CreateParameterForm()}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = CreateParameterForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'create_parameter_form': CreateParameterForm(),
                'success': 'Succesfully created new parameter'
            }
        else:
            context = {'create_parameter_form': form}
        return TemplateResponse(request, self.template_name, context)

