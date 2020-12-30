from django.views import View
from django.template.response import TemplateResponse

from ..models import *
from ..forms import *

class BikeEditView(View):

    template_name = 'firmware/bike.html'

    def get_parameter(self, bike_id, row, column):
        try:
            item = BikeParameter.objects.get(bike_id=bike_id, row=row, column=column)
        except BikeParameter.DoesNotExist:
            return '-'
        else:
            parameter = Parameter.objects.get(pk=item.parameter_id)
            return parameter.id


    def get_bike(self, pk):
        bike = Bike.objects.get(pk=pk)
        Forms = []

        for row in range(6):
            forms = []
            for column in range(31):
                initial = {
                    'choice': self.get_parameter(pk, row, column),
                    'row': row,
                    'column': column
                }
                form = SelectParameterForm(initial=initial)
                forms.append(form)
            Forms.append(forms)

        bike_data = {
            'bike': bike, 
            'row': range(6),
            'column': range(31),
            'Forms': Forms,
        }
        return bike_data

    def get(self, request, pk):
        bike_data = self.get_bike(pk)
        context = {'bike': bike_data}
        return TemplateResponse(request, self.template_name, context)


    def post(self, request, pk):
        form = SelectParameterForm(data=request.POST)
        if form.is_valid():
            form.save(pk)
            bike_data = self.get_bike(pk)
            context = {'success': 'Changed', 'bike': bike_data}
            return TemplateResponse(request, self.template_name,    context)        
        bike_data = self.get_bike(pk)
        context = {'bike': bike_data}
        return TemplateResponse(request, self.template_name, context)


