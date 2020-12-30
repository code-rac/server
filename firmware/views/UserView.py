from django.views import View
from django.template.response import TemplateResponse
from ..models import User
from ..forms import *
from . import util
from django.db.models import Q

class UserView(View):

    template_name = 'firmware/user.html'

    def get_users(self):
        users = User.objects.filter(groups__name__in=['user']).all()
        return users

    def get_user_from_form(self, form):
        try:
            users = User.objects.filter(
                Q(code__contains=form.cleaned_data['code']) & 
                Q(phone__contains=form.cleaned_data['phone']))
        except User.DoesNotExist:
            users = []

        return self.get_items(users)


    def get_items(self, users):
        items = []
        for user in users:
            item = {
                'id': user.id,
                'username': user.username, 
                'code': user.code, 
                'phone': user.phone, 
                'store_name': user.store_name, 
                'address': user.address, 
                'start_at': str(user.start_at), 
                'choice': util.get_choice(user)
            }
            items.append(item)
        return items
        
    def get(self, request):
        users = self.get_users()
        items = self.get_items(users)
        context = {
            'items': items, 
            'search_user_form': SearchUserForm()
        }
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = SearchUserForm(request.POST)
        if form.is_valid():
            items = self.get_user_from_form(form)

            if items:
                context = {
                    'search_user_form': SearchUserForm(),
                    'items': items
                }
            else:
                context = {
                    'search_user_form': form, 
                    'error': 'User does not exist'
                }
        else:
            context = {
                'search_user_form': form,
            }
        return TemplateResponse(request, self.template_name, context)
