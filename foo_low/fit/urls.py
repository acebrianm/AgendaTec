from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^my_account/$', views.my_account, name='my_account'),
]
