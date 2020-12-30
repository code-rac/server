from django.views import View
from django.template.response import TemplateResponse
from ..forms import CreateBikeForm

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator([csrf_exempt], name='dispatch')
class CreateBikeView(View):

    template_name = 'firmware/bike.html'

    def get(self, request):
        context = {'create_bike_form': CreateBikeForm()}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = CreateBikeForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'create_bike_form': CreateBikeForm(),
                'success': 'Succesfully created new bike'
            }
        else:
            context = {'create_bike_form': form}
        return TemplateResponse(request, self.template_name, context)

