from django.conf.urls import url
from rest_framework.authtoken import views as auth_views


from . import views

urlpatterns = [
    url(r'^api$', views.register, name='register'),
    url(r'^api/(?P<pk>[0-9]+)$', views.validate, name='register'),
    url(r'api-token-auth/', auth_views.obtain_auth_token),
]
