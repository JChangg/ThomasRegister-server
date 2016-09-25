from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PersonListView.as_view(), name='users'),
]

