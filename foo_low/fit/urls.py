from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^list/(?P<tag>[0-9a-zA-Z_]+)/$', views.list, name="list"),
    url(r'^edit_event/(?P<event>[0-9]+)/$', views.edit_event,
        name="edit_event"),
    url(r'^delete_event/(?P<event>[0-9]+)/$', views.delete_event,
        name="delete_event"),
    url(r'^detail/(?P<event>[0-9a-zA-Z_]+)/$', views.detail_event, name="detail"),
    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^add_tag/$', views.add_tag, name='add_tag'),
    url(r'^edit_tag/(?P<tag>[0-9]+)/$', views.edit_tag, name="edit_tag"),
    url(r'^delete_tag/(?P<tag>[0-9]+)/$', views.delete_tag, name="delete_tag"),
]
