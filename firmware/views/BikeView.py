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
                'name': bike.name,
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
