from django.views import View
from django.template.response import TemplateResponse

from . import util
from ..models import *
from ..forms import *

class UserDetailView(View):
    
    template_name = 'firmware/user.html'

    def get_user(self, pk):
        user = User.objects.get(pk=pk)
        initial = {'username' : user.username, 'choice': util.get_choice(user)}
        form = ReadWriteForm(initial=initial)
        form.username = user.username
        item = {
            'id': user.id,
            'username': user.username, 
            'code': user.code, 
            'phone': user.phone, 
            'store_name': user.store_name, 
            'address': user.address, 
            'start_at': str(user.start_at),
            'form': form
        }
        return item

    def get(self, request, pk):
        item = self.get_user(pk)
        context = {'item': item}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request, pk):
        form = ReadWriteForm(data=request.POST)        
        if form.is_valid():
            form.save()
            item = self.get_user(pk)
            context = {'success': 'Changed to {}'.format(str(form.cleaned_data['choice'])) , 'item': item}
            return TemplateResponse(request, self.template_name, context)        

        item = self.get_user(pk)
        context = {'item': item}
        return TemplateResponse(request, self.template_name, context)
