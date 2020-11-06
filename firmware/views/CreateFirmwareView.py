from django.views import View
from django.template.response import TemplateResponse
from ..forms import CreateFirmwareForm

class CreateFirmwareView(View):

    template_name = 'firmware/firmware.html'

    def get(self, request):
        context = {'create_firmware_form': CreateFirmwareForm()}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = CreateFirmwareForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'create_firmware_form': CreateFirmwareForm(),
                       'success': 'Succesfully created new firmware'}
        else:
            context = {'create_firmware_form': form}
        return TemplateResponse(request, self.template_name, context)