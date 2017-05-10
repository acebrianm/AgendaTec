from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^add_tag/$', views.add_tag, name='add_tag'),
    url(r'^edit_tag/(?P<tag>[0-9]+)/$', views.edit_tag, name="edit_tag"),
    url(r'^delete_tag/(?P<tag>[0-9]+)/$', views.delete_tag, name="delete_tag"),
]
