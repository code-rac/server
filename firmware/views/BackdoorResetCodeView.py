from ..forms import *
from ..models import Code
from django.views import View
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.template.response import TemplateResponse


class BackdoorResetCodeView(View):

    template_name = 'firmware/code.html'

    def post(self, request):
        Code.objects.all().delete()
        context = {'success': 'Successfully cleaned database'}
        return TemplateResponse(request, self.template_name, context)    
