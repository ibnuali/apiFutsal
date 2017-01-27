from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ProvinceViewSet(viewsets.ModelViewSet):

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class PlayerViewSet(viewsets.ModelViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class FieldLocViewSet(viewsets.ModelViewSet):

    queryset = FieldLocation.objects.all()
    serializer_class = FieldLocSerializer

class FieldViewSet(viewsets.ModelViewSet):

    queryset = Field.objects.all()
    serializer_class = FieldSerializer

class FieldPhotosViewSet(viewsets.ModelViewSet):

    queryset = FieldPhotos.objects.all()
    serializer_class = FieldPhotoSerializer

class CreateRoomViewSet(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = ListRoomSerializer

class PartyViewSet(viewsets.ModelViewSet):

    queryset = Party.objects.all()
    serializer_class = PartySerializer

class FriendViewSet(viewsets.ModelViewSet):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class JoinPartyViewSet(viewsets.ModelViewSet):

    queryset = JoinParty.objects.all()
    serializer_class = JoinPartySerializer

class LevelViewSet(viewsets.ModelViewSet):

    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelHistoryViewSet(viewsets.ModelViewSet):

    queryset = LevelHistory.objects.all()
    serializer_class = LevelHistorySerializer

class LevelViewSet(viewsets.ModelViewSet):

    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelHistoryViewSet(viewsets.ModelViewSet):

    queryset = LevelHistory.objects.all()
    serializer_class = LevelHistorySerializer

class RatingHistoryViewSet(viewsets.ModelViewSet):

    queryset = RatingHistory.objects.all()
    serializer_class = RatingHistorySerializer

class FriendViewSet(viewsets.ModelViewSet):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class RequiredPositionsViewSet(viewsets.ModelViewSet):

    queryset = RequiredPositions.objects.all()
    serializer_class = RequiredPositionsSerializer

class StoreViewSet(viewsets.ModelViewSet):

    queryset = Friend.objects.all()
    serializer_class = StoreSerializer


