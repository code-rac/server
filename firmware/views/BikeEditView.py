from django.views import View
from django.template.response import TemplateResponse
from django.db import IntegrityError

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

    def get_bike_parameters(self, pk):
        bike_parameters = BikeParameter.objects.filter(bike_id=pk).all()

        forms = []
        for bp in bike_parameters:
            parameter = Parameter.objects.get(pk=bp.parameter_id)
            initial = {
                'bike_id': pk,
                'parameter_id': bp.parameter_id,
                'name': parameter.name,
                'name_vn': parameter.name_vn,
                'action': 'expression_edit',
                'expression': bp.expression
            }
            form = ExpressionEditForm(initial=initial)
            forms.append(form)
        return forms

    def get_bike(self, pk):
        bike = Bike.objects.get(pk=pk)
        Forms = []

        for row in range(6):
            forms = []
            for column in range(31):
                initial = {
                    'choice': self.get_parameter(pk, row, column),
                    'row': row,
                    'column': column,
                    'action': 'select_parameter'
                }
                form = SelectParameterForm(initial=initial)
                forms.append(form)
            Forms.append(forms)


        bike_data = {
            'bike': bike, 
            'row': range(6),
            'column': range(31),
            'Forms': Forms,
            'bike_parameter_forms': self.get_bike_parameters(pk),
        }
        return bike_data

    def get(self, request, pk):
        bike_data = self.get_bike(pk)
        context = {'bike': bike_data}
        return TemplateResponse(request, self.template_name, context)


    def select_parameter(self, request, pk):
        form = SelectParameterForm(data=request.POST)
        if form.is_valid():
            try:
                form.save(pk)
            except IntegrityError:
                bike_data = self.get_bike(pk)
                context = {'error': 'Duplicated parameter', 'bike': bike_data}
                return TemplateResponse(request, self.template_name, context)        
            else:
                bike_data = self.get_bike(pk)
                context = {'success': 'Changed parameter', 'bike': bike_data}
                return TemplateResponse(request, self.template_name, context)      
        bike_data = self.get_bike(pk)
        context = {'bike': bike_data}
        return TemplateResponse(request, self.template_name, context)


    def expression_edit(self, request, pk):
        form = ExpressionEditForm(data=request.POST)
        if form.is_valid():
            form.save()
            context = {'success': 'Changed expression', 'bike': self.get_bike(pk)}
            return TemplateResponse(request, self.template_name, context)        
        context = {'bike': self.get_bike(pk)}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request, pk):
        action = request.POST['action']     
        if action == 'select_parameter':
            return self.select_parameter(request, pk)
        elif action == 'expression_edit':
            return self.expression_edit(request, pk)
        else:
            context = {'bike': self.get_bike(pk), 'error': 'Unknown action'}
            return TemplateResponse(request, self.template_name, context)

