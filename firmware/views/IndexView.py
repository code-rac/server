from django.views import View
from django.db.models import Sum
from django.template.response import TemplateResponse
from ..models import Firmware

class IndexView(View):
    template_name = 'firmware/index.html'
    
    def get(self, request):
        context = {}
        return TemplateResponse(request, self.template_name, context)