from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^register/', include('register.urls')),
    url(r'^admin/', admin.site.urls),
]
