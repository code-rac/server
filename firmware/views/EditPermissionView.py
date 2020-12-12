from django.views import View
from django.template.response import TemplateResponse
from ..models import User

class EditPermissionView(View):

    template_name = 'firmware/edit-permission.html'


    def get_users(self):
        users = User.objects.filter(groups__name__in=['user']).all()
        return users

        
    def get(self, request):
        users = self.get_users()
        context = {'users': users}
        return TemplateResponse(request, self.template_name, context)


    def post(self, request):
        

        return TemplateResponse(request, self.template_name, context)

