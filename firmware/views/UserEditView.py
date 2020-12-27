from django.views import View
from django.template.response import TemplateResponse

from ..models import *
from ..forms import *

class UserEditView(View):

    template_name = 'firmware/user.html'

    def get_user(self, pk):
        user = User.objects.get(pk=pk)
        initial = {
            'pk': user.pk,
            'username' : user.username, 
            'phone': user.phone,
            'store_name': user.store_name,
            'address': user.address,
        }
        form = UserEditForm(initial=initial)
        return form

    def get(self, request, pk):
        form = self.get_user(pk)
        context = {'user_edit_form': form}
        return TemplateResponse(request, self.template_name, context)


    def post(self, request, pk):
        form = UserEditForm(data=request.POST)        
        if form.is_valid():
            form.save()
            context = {'success': 'Changed', 'user_edit_form': form}
            return TemplateResponse(request, self.template_name, context)        

        context = {'user_edit_form': form}
        return TemplateResponse(request, self.template_name, context)
