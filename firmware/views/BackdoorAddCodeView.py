from ..forms import *
from ..models import Code
from django.views import View
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.template.response import TemplateResponse

@method_decorator([csrf_exempt], name='dispatch')
class BackdoorAddCodeView(View):

    template_name = 'firmware/code.html'

    def get_codes(self):
        objects = Code.objects.all()
        return objects

    def get(self, request):
        codes = self.get_codes()

        context = {'backdoor_add_code_form':BackdoorAddCodeForm(), 'codes': codes}
        return TemplateResponse(request, self.template_name, context)    


    def post(self, request):        
        form = BackdoorAddCodeForm(request.POST)
        codes = self.get_codes()

        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                context = {'backdoor_add_code_form': BackdoorAddCodeForm(), 'error':'Duplicated code', 'codes': codes}
            else:
                context = {'backdoor_add_code_form': BackdoorAddCodeForm(), 'success':'Successfully added', 'codes': codes}

            return TemplateResponse(request, self.template_name, context)        

        context = {'backdoor_add_code_form': form, 'codes': codes}
        return TemplateResponse(request, self.template_name, context)
