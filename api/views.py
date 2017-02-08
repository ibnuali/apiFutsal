from django.shortcuts import render
from rest_framework import generics,views
from rest_framework.response import Response
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

class CreatePlayerView(views.APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            player = serializer.save(created_at=timezone.now(),player_photo="urldefault")
            output_serializer = PlayerDetailSerializer(player)
            return Response(output_serializer.data)
        else:
            return Response(serializer.errors)

class SignInPlayerView(views.APIView):
    def get(self, request, username, password):
        try:
            player = Player.SignIn(username,password)
        except player.DoesNotExist:
            return HttpResponse(status=404)
        serializer = PlayerDetailSerializer(player, many=True)
        return Response(serializer.data)

class UpdatePlayerView(generics.RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerDataSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class GetPlayerView(views.APIView):
    def get(self, request, username):
        try:
            player = Player.objects.filter(player_username = username)
        except player.DoesNotExist:
            return HttpResponse(status=404)
        serializer = PlayerSerializer(player, many=True)
        return Response(serializer.data)

class FriendList(generics.ListCreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendListSerializer

class FieldLocList(generics.ListAPIView):
    queryset = FieldLocation.objects.all()
    serializer_class = FieldLocSerializer

class FieldList(generics.ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

class FieldPhotosList(generics.ListAPIView):
    queryset = FieldPhotos.objects.all()
    serializer_class = FieldPhotoSerializer

class CreateRoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = ListRoomSerializer

class PartyList(generics.ListAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

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

class RequiredPositionsList(generics.ListAPIView):
    queryset = RequiredPositions.objects.all()
    serializer_class = RequiredPositionsSerializer

class StoreList(generics.ListAPIView):
    queryset = Friend.objects.all()
    serializer_class = StoreSerializer
