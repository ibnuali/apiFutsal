from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        depth = 2

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ('id_province','name_province')
        depth = 1

class District(serializers.ModelSerializer):

     class Meta:
        model = Province
        fields = '__all__'
        depth = 1

class GenderSerializer(serializers.ModelSerializer):

     class Meta:
        model = Genders
        fields = '__all__'

class PlayerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('id_player','player_name','player_photo')

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

class FieldLocSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldLocation
        fields = '__all__'

class CreateRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

class ListRoomSerializer(serializers.ModelSerializer):

    id_player = PlayerDetailSerializer()
    id_field = FieldLocSerializer()

    class Meta:
        model = Room
        fields = (
                    'id_player','id_field','room_name','room_stadium',
                    'room_address','room_duration','required_level_min',
                    'required_level_max','required_gender','required_age_min',
                    'required_age_max','required_slot','room_status','room_created',
                    'room_updated'
                 )

class PartySerializer(serializers.ModelSerializer):

    id_player = PlayerDetailSerializer()

    class Meta:
        model = Party
        fields = ('id_player','party_name')
