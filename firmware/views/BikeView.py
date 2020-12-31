from django.views import View
from django.template.response import TemplateResponse
from ..forms import *
from ..models import *
from . import util
from django.db.models import Q

class BikeView(View):

    template_name = 'firmware/bike.html'

    def get_bikes(self):
        bikes = Bike.objects.all()
        return bikes


    def get_items(self, bikes):
        items = []
        for bike in bikes:
            item = {
                'id': bike.id,
                'ecu_id': bike.ecu_id,
                'name': bike.name,
                'generation': bike.generation,
                'code': bike.code,
                'start_at': bike.start_at,
                'is_used': bike.is_used,
                'cc': bike.cc,
                'form': self.get_bike_clone_form(bike.id)
            }
            items.append(item)
        return items
        
    def get(self, request):
        bikes = self.get_bikes()
        items = self.get_items(bikes)
        context = {
            'items': items, 
        }
        return TemplateResponse(request, self.template_name, context)

    def get_bike_clone_form(self, pk):
        initial = {'pk': pk}
        return BikeCloneForm(initial=initial)

    def post(self, request):
        form = BikeCloneForm(request.POST)
        if form.is_valid():
            form.save()
            bikes = self.get_bikes()
            context = {
                'items': self.get_items(bikes),
                'success': 'Succesfully cloned'
            }
            return TemplateResponse(request, self.template_name, context)
        bikes = self.get_bikes()
        context = {'items': self.get_items(bikes), 'error': 'Cloned failed'}
        return TemplateResponse(request, self.template_name, context)