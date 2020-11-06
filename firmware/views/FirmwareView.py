from django.views import View
from django.template.response import TemplateResponse
from ..models import Firmware
from ..forms import FirmwareSearchForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator([csrf_exempt], name='dispatch')
class FirmwareView(View):

    template_name = 'firmware/firmware.html'

    def get_firmwares(self):
        objects = Firmware.objects.all()
        return objects

    def get_firmware_by_name(self, name):
        try:
            firmware = Firmware.objects.get(name=name)
        except Firmware.DoesNotExist:
            firmware = None
        return firmware

    def get(self, request):
        firmwares = self.get_firmwares()
        context = {
            'firmwares': firmwares, 
            'search_firmware_form': FirmwareSearchForm()
        }

        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = FirmwareSearchForm(request.POST)

        if form.is_valid():
            firmware = self.get_firmware_by_name(form.cleaned_data['name'])
            if form.cleaned_data['json']:
                if firmware:
                    return JsonResponse({'offset': firmware.offset})
                else:
                    return JsonResponse({'error': 'Firmware does not exist'}) 

            if firmware:
                context = {
                    'search_firmware_form': FirmwareSearchForm(),
                    'firmware': firmware
                }

            else:
                context = {
                    'search_firmware_form': form, 
                    'error': 'Firmware does not exist'
                }

        else:
            context = {
                'search_firmware_form': form,
            }
            
        return TemplateResponse(request, self.template_name, context)