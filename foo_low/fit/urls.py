from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^list/(?P<tag>[0-9a-zA-Z_]+)/$', views.list, name="list"),
]
