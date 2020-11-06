from django.views import View
from django.db.models import Sum
from django.template.response import TemplateResponse
from ..models import Firmware
import os

class IndexView(View):
    template_name = 'firmware/index.html'
    
    def get(self, request):
        context = {}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        Firmware.objects.all().delete()
        folder = 'media/'
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))

        context = {'success': 'Successfully cleaned database'}
        return TemplateResponse(request, self.template_name, context)
