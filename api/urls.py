from django.conf.urls import url,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^city/$', views.CityListView.as_view()),
	url(r'^country/$', views.CountryListView.as_view()),
	url(r'^province/$', views.ProvinceListView.as_view()),
	url(r'^signup/$', views.CreatePlayerView.as_view()),
	url(r'^editprofile/(?P<pk>[0-9]+)$', views.UpdatePlayerView.as_view()),
	url(r'^fieldloc/$', views.FieldLocList.as_view()),
	url(r'^field/$', views.FieldList.as_view()),
	url(r'^room/$', views.CreateRoomList.as_view()),
	url(r'^party/$', views.PartyList.as_view()),
	url(r'^fieldphotos/$', views.FieldPhotosList.as_view()),
	url(r'^room/$', views.FriendList.as_view()),
	url(r'^friend/$', views.FriendList.as_view()),
	url(r'^joinparty/$', views.JoinPartyList.as_view()),
	url(r'^level/$', views.LevelList.as_view()),
	url(r'^levelhistory/$', views.LevelHistoryList.as_view()),
	url(r'^ratinghistory/$', views.RatingHistoryList.as_view()),
	url(r'^requiredposition/$', views.RequiredPositionsList.as_view()),
	url(r'^store/$', views.StoreList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
