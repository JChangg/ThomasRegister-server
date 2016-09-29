from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/card$', views.register, name='register'),
    url(r'^card/(?P<pk>[0-9]+)$', views.validate, name='register'),
]
