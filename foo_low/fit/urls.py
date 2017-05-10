from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^list/(?P<tag>[0-9a-zA-Z_]+)/$', views.list, name="list"),
    url(r'^detail/(?P<event>[0-9a-zA-Z_]+)/$', views.detail_event, name="detail"),
    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
]
