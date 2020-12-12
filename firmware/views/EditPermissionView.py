from django.views import View
from django.template.response import TemplateResponse
from ..models import User
from ..forms import *

class EditPermissionView(View):

    template_name = 'firmware/edit-permission.html'


    def get_users(self):
        users = User.objects.filter(groups__name__in=['user']).all()
        return users

    def get_choice(self, user):
        if user.readable and user.writable:
            return 'Read/Write'
        elif not user.readable and user.writable:
            return 'Write'
        elif user.readable and not user.writable:
            return 'Read'
        elif not user.readable and not user.writable:
            return 'None'
        else:
            raise NotImplementedError

    def get_items(self, users):
        items = []
        for user in users:
            initial = {'username' : user.username, 'choice': self.get_choice(user)}
            form = ReadWriteForm(initial=initial)
            form.username = user.username
            item = {'username': user.username, 'code': user.code, 'form': form}
            items.append(item)
        return items
        
    def get(self, request):
        users = self.get_users()
        items = self.get_items(users)
        context = {'items': items}
        return TemplateResponse(request, self.template_name, context)


    def post(self, request):
        
        form = ReadWriteForm(data=request.POST)        
        if form.is_valid():
            form.save()
            users = self.get_users()
            items = self.get_items(users)            
            context = {'form': form, 'success': 'Changed', 'items': items}
            return TemplateResponse(request, self.template_name, context)        

        users = self.get_users()
        items = self.get_items(users)            
        context = {'form': form, 'items': items}
        return TemplateResponse(request, self.template_name, context)
