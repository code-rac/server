from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^firmware$', FirmwareView.as_view(), name='firmware'),
    url(r'^create-firmware$', CreateFirmwareView.as_view(), name='create-firmware'),
    url(r'^firmware-detail/(?P<pk>\d+)/$', FirmwareDetailView.as_view(), name='firmware-detail'),
    url(r'^backdoor-add-code$', BackdoorAddCodeView.as_view(), name='backdoor-add-code'),
]