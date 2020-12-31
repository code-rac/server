from django.views import View
from django.template.response import TemplateResponse
from ..forms import *
from ..models import *
from . import util
from django.db.models import Q

class BikeView(View):

    template_name = 'firmware/bike.html'

    def get_items(self):
        items = []
        for bike in Bike.objects.all():
            item = {
                'id': bike.id,
                'ecu_id': bike.ecu_id,
                'name': bike.name,
                'generation': bike.generation,
                'code': bike.code,
                'start_at': bike.start_at,
                'is_used': bike.is_used,
                'cc': bike.cc,
                'clone_form': BikeCloneForm(initial={'action': 'clone', 'pk': bike.id}),
                'delete_form': DeleteBikeForm(initial={'action': 'delete', 'pk': bike.id})
            }
            items.append(item)
        return items
        
    def get(self, request):
        items = self.get_items()
        context = {
            'items': items, 
        }
        return TemplateResponse(request, self.template_name, context)

    def clone_bike(self, request):
        form = BikeCloneForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'items': self.get_items(),
                'success': 'Succesfully cloned'
            }
            return TemplateResponse(request, self.template_name, context)
        context = {'items': self.get_items(), 'error': 'Cloned failed'}
        return TemplateResponse(request, self.template_name, context)

    def delete_bike(self, request):
        form = DeleteBikeForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'items': self.get_items(),
                'success': 'Deleted'
            }
            return TemplateResponse(request, self.template_name, context)
        context = {
            'items': self.get_items(),
            'error': 'Deleted failed'
        }
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        action = request.POST['action']     
        if action == 'clone':
            return self.clone_bike(request)
        elif action == 'delete':
            return self.delete_bike(request)
        else:
            context = {
                'items': self.get_items(),
                'error': 'Deleted failed'
            }
            return TemplateResponse(request, self.template_name, context)

