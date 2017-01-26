from django.conf.urls import url,include
from rest_framework import routers
from api import views


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


