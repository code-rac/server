from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^firmware$', FirmwareView.as_view(), name='firmware'),
    url(r'^create-firmware$', CreateFirmwareView.as_view(), name='create-firmware'),
    url(r'^firmware-detail/(?P<pk>\d+)/$', FirmwareDetailView.as_view(), name='firmware-detail'),
    url(r'^backdoor-add-code$', BackdoorAddCodeView.as_view(), name='backdoor-add-code'),
    url(r'^backdoor-reset-code$', BackdoorResetCodeView.as_view(), name='backdoor-reset-code'),
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^login$', LoginView.as_view(), name='login'), 
    # url(r'^logout/$', LogoutView.as_view(), {'next_page': '/', 'template_name': 'firmware:index', 'extra_context': {'success': 'Logged out'}}, name='logout'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]