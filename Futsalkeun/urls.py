from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'province,', views.ProvinceViewSet)
router.register(r'player,', views.PlayerViewSet)
router.register(r'field,', views.FieldLocViewSet)
router.register(r'room', views.CreateRoomViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


