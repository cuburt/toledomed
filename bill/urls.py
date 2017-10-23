from django.conf.urls import url
from . import views


app_name = 'bill'

urlpatterns = [

    url(r'^user=(?P<identity_id>[0-9]+)/$', views.index, name='index'),
    url(r'^view_bill/user=(?P<identity_id>[0-9]+)/$', views.generate_bill, name='generate_bill'),

]
