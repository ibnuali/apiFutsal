from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from django.utils import timezone

class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ProvinceListView(generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class CreatePlayerView(generics.CreateAPIView):
    serializer_class = PlayerSerializer
    def perform_create(self, serializer):
        serializer.save(created_at=timezone.now(),player_photo="urldefault")

class UpdatePlayerView(generics.RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class FieldLocList(generics.ListAPIView):
    queryset = FieldLocation.objects.all()
    serializer_class = FieldLocSerializer

class FieldList(generics.ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

class FieldPhotosList(generics.ListAPIView):
    queryset = FieldPhotos.objects.all()
    serializer_class = FieldPhotoSerializer

class CreateRoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = ListRoomSerializer

class PartyList(generics.ListAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class FriendList(generics.ListAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class JoinPartyList(generics.ListAPIView):
    queryset = JoinParty.objects.all()
    serializer_class = JoinPartySerializer

class LevelList(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelHistoryList(generics.ListAPIView):
    queryset = LevelHistory.objects.all()
    serializer_class = LevelHistorySerializer

class LevelList(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelHistoryList(generics.ListAPIView):
    queryset = LevelHistory.objects.all()
    serializer_class = LevelHistorySerializer

class RatingHistoryList(generics.ListAPIView):
    queryset = RatingHistory.objects.all()
    serializer_class = RatingHistorySerializer

class FriendList(generics.ListAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class RequiredPositionsList(generics.ListAPIView):
    queryset = RequiredPositions.objects.all()
    serializer_class = RequiredPositionsSerializer

class StoreList(generics.ListAPIView):
    queryset = Friend.objects.all()
    serializer_class = StoreSerializer
