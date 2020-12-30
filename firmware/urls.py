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
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^user/$', UserView.as_view(), name='user'),
    url(r'^user-detail/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^user-edit/(?P<pk>\d+)/$', UserEditView.as_view(), name='user-edit'),
    url(r'^create-parameter$', CreateParameterView.as_view(), name='create-parameter'),
    url(r'^parameter/$', ParameterView.as_view(), name='parameter'),
    url(r'^parameter-edit/(?P<pk>\d+)/$', ParameterEditView.as_view(), name='parameter-edit'),
    url(r'^create-bike$', CreateBikeView.as_view(), name='create-bike'),
    url(r'^bike/$', BikeView.as_view(), name='bike'),
    url(r'^bike-edit/(?P<pk>\d+)/$', BikeEditView.as_view(), name='bike-edit'),
]