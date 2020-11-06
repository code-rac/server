from django.views.generic.detail import DetailView
from ..models import *

class FirmwareDetailView(DetailView):
    
    model = Firmware
    template_name = 'firmware/firmware.html'