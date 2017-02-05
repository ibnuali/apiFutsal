from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from api import views, urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(urls))
]


