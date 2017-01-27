from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'province,', views.ProvinceViewSet)
router.register(r'player,', views.PlayerViewSet)
router.register(r'fieldloc,', views.FieldLocViewSet)
router.register(r'field,', views.FieldViewSet)
router.register(r'room', views.CreateRoomViewSet)
router.register(r'party', views.PartyViewSet)
router.register(r'FieldPhotos,', views.FieldPhotosViewSet)
router.register(r'room', views.FriendViewSet)
router.register(r'friend', views.FriendViewSet)
router.register(r'JoinParty', views.JoinPartyViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'RatingHistory', views.LevelHistoryViewSet)
router.register(r'Friend', views.RatingHistoryViewSet)
router.register(r'requiredposition', views.RequiredPositionsViewSet)
router.register(r'store', views.StoreViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


