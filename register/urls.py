from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api$', views.register, name='register'),
    url(r'^api/(?P<pk>[0-9]+)$', views.validate, name='register'),
]
