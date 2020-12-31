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
            return '-', False
        else:
            parameter = Parameter.objects.get(pk=item.parameter_id)
            return parameter.id, item.is_used

    def get_bike_parameters(self, pk):
        bpes = BikeParameterExpression.objects.filter(bike_id=pk).all()

        forms = []
        for bpe in bpes:
            parameter = Parameter.objects.get(pk=bpe.parameter_id)
            bps = BikeParameter.objects.filter(bike_id=pk, parameter_id=bpe.parameter_id).all()

            initial = {
                'bike_id': pk,
                'parameter_id': bpe.parameter_id,
                'name': parameter.name,
                'name_vn': parameter.name_vn,
                'action': 'expression_edit',
                'expression': bpe.expression,
                'variable_name': ', '.join(bp.name for bp in bps),
                'is_used': bpe.is_used
            }
            form = ExpressionEditForm(initial=initial)
            forms.append(form)
        return forms

    def get_bike_edit_form(self, pk):
        bike = Bike.objects.get(pk=pk)
        initial = {
            'action': 'bike_edit',
            'pk': pk,
            'name': bike.name,
            'ecu_id': bike.ecu_id,
            'generation': bike.generation,
            'code': bike.code,
            'start_at': bike.start_at,
            'is_used': bike.is_used,
            'cc': bike.cc
        }
        return BikeEditForm(initial=initial)

    def get_bike(self, pk):
        bike = Bike.objects.get(pk=pk)
        Forms = []

        for row in range(6):
            forms = []
            for column in range(31):
                choice, is_used = self.get_parameter(pk, row, column)
                initial = {
                    'choice': choice,
                    'row': row,
                    'column': column,
                    'action': 'select_parameter',
                    'is_used': is_used
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
            'bike_edit_form': self.get_bike_edit_form(pk)
        }
        return bike_data

    def get(self, request, pk):
        bike_data = self.get_bike(pk)
        context = {'bike': bike_data}
        return TemplateResponse(request, self.template_name, context)


    def select_parameter(self, request, pk):
        form = SelectParameterForm(data=request.POST)
        if form.is_valid():
            form.save(pk)      
            context = {'success': 'Changed parameter', 'bike': self.get_bike(pk)}
            return TemplateResponse(request, self.template_name, context)      
        context = {'bike': self.get_bike(pk)}
        return TemplateResponse(request, self.template_name, context)


    def expression_edit(self, request, pk):
        form = ExpressionEditForm(data=request.POST)
        if form.is_valid():
            form.save()
            context = {'success': 'Changed expression', 'bike': self.get_bike(pk)}
            return TemplateResponse(request, self.template_name, context)        
        context = {'bike': self.get_bike(pk)}
        return TemplateResponse(request, self.template_name, context)


    def bike_edit(self, request, pk):
        form = BikeEditForm(data=request.POST)        
        if form.is_valid():
            form.save()
            context = {'success': 'Changed bike', 'bike': self.get_bike(pk)}
            return TemplateResponse(request, self.template_name, context)        
        bike_data = self.get_bike(pk)
        bike_data['bike_edit_form'] = form
        context = {'bike': bike_data}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request, pk):
        action = request.POST['action']     
        if action == 'select_parameter':
            return self.select_parameter(request, pk)
        elif action == 'expression_edit':
            return self.expression_edit(request, pk)
        elif action == 'bike_edit':
            return self.bike_edit(request, pk)
        else:
            context = {'bike': self.get_bike(pk), 'error': 'Unknown action'}
            return TemplateResponse(request, self.template_name, context)

