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

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

class FieldLocSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldLocation
        fields = '__all__'

class CreateRoomSerializer(serializers.ModelSerializer):

    # Player = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='player_name'
    #  )

    # field = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name_field'
    #  )
    Player = PlayerSerializer(source='id_player', read_only=True)

    class Meta:
        model = Room
        fields = (
                    'Player','room_name','room_stadium',
                    'room_address','room_duration','required_level_min',
                    'required_level_max','required_gender','required_age_min',
                    'required_age_max','required_slot','room_status','room_created',
                    'room_updated'
                 )

