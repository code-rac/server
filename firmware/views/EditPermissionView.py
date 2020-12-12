from django.views import View
from django.template.response import TemplateResponse
from ..models import User

class EditPermissionView(View):

    template_name = 'firmware/edit-permission.html'


    def get_users(self):
        objects = User.objects.all()
        return objects

        
    def get(self, request):
        users = self.get_users()

        context = {}
        return TemplateResponse(request, self.template_name, context)
