from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.template.response import TemplateResponse

from ..models import *

@method_decorator([csrf_exempt], name='dispatch')
class BikeJsonView(View):

    def get_index(self, bike_id, parameter_id, row):
        columns = []
        for bp in BikeParameter.objects.filter(bike_id=bike_id, parameter_id=parameter_id, row=row).all():
            if bp.is_used:
                columns.append(str(bp.column))
        return ','.join(columns)

    def get_formula(self, bike_id, parameter_id):
        bpe = BikeParameterExpression.objects.get(bike_id=bike_id, parameter_id=parameter_id)
        if bpe.is_used:
            return bpe.expression
        return ''

    def get(self, request, ecu_id):
        data = {}
        bike = Bike.objects.get(ecu_id=ecu_id)
        for row in range(6):
            key = 'table_{}'.format(row+1)
            value = {}
            for parameter_id in list(set([bp.parameter_id for bp in BikeParameter.objects.filter(bike_id=bike.id, row=row).all()])):
                p = Parameter.objects.get(pk=parameter_id)
                index = self.get_index(bike.id, parameter_id, row)
                if index:
                    value[p.name] = {
                        'index': index,
                        'description': p.description,
                        'name': p.name_vn,
                        'unit': p.unit,
                        'upper': str(p.upper),
                        'lower': str(p.lower),
                        'recommend': str(p.recommend),
                        'formula': self.get_formula(bike.id, parameter_id),
                    }
            data[key] = value

        return JsonResponse(data)
