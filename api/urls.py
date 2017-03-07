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
    url(r'^signin/(?P<username>.+)/(?P<password>.+)/$', views.SignInPlayerView.as_view()),
    url(r'^getplayerbyid/(?P<pk>.+)/$', views.GetPlayerByIdView.as_view()),
    url(r'^getplayerbyusername/(?P<username>.+)/$', views.GetPlayerByUsernameView.as_view()),
    url(r'^friend/$', views.FriendList.as_view()),
    url(r'^room/$', views.CreateRoomListView.as_view()),
    url(r'^getroom/(?P<pk>[0-9]+)$', views.RoomDetailView.as_view()),
    url(r'^updateroom/(?P<pk>[0-9]+)$', views.UpdateRoomView.as_view()),
    url(r'^joinroom/$', views.JoinRoomView.as_view()),
	url(r'^team/$', views.TeamList.as_view()),
	url(r'^jointeam/$', views.JoinTeamList.as_view()),
	url(r'^level/$', views.LevelList.as_view()),
	url(r'^levelhistory/$', views.LevelHistoryList.as_view()),
	url(r'^ratinghistory/$', views.RatingHistoryList.as_view()),
	url(r'^requiredposition/$', views.RequiredPositionsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
