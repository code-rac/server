from django.views import View
from django.template.response import TemplateResponse
from ..models import Firmware
from ..forms import FirmwareSearchForm

class FirmwareView(View):

    template_name = 'firmware/firmware.html'

    def get_firmware(self):
        objects = Firmware.objects.all()
        return objects

    def get(self, request):
        firmwares = self.get_firmware()
        context = {
            'firmwares': firmwares, 
            'search_firmware_form': FirmwareSearchForm()
        }

        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = FirmwareSearchForm(request.POST)

        if form.is_valid():

            try:
                firmware = Firmware.objects.get(name=form.cleaned_data['name'])
                context = {
                    'search_firmware_form': FirmwareSearchForm(),
                    'firmware': firmware
                }
            except Firmware.DoesNotExist:
                context = {
                    'search_firmware_form': form, 
                    'error': 'Firmware does not exist'
                }

        else:
            context = {
                'search_firmware_form': form,
            }
        return TemplateResponse(request, self.template_name, context)