from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class District(serializers.ModelSerializer):
     class Meta:
        model = Province
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
     class Meta:
        model = Genders
        fields = '__all__'

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('created_at','updated_at')

class PlayerPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPosition
        fields = '__all__'

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class FieldLocSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldLocation
        fields = '__all__'

class FieldPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldPhotos
        fields = '__all__'

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class ListRoomSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(many=True, read_only=True,source='id_player')
    class Meta:
        model = Room
        fields = (
                    'player','id_field_location','room_name','room_stadium',
                    'room_address','room_duration','required_level_min',
                    'required_level_max','required_gender','required_age_min',
                    'required_age_max','required_slot','room_status','room_created',
                    'room_updated'
                 )

class PartySerializer(serializers.ModelSerializer):
    id_player = PlayerSerializer()
    class Meta:
        model = Party
        fields = '__all__'

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

class JoinPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinParty
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class LevelHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelHistory
        fields = '__all__'

class JoinRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRoom
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingHistory
        fields = '__all__'

class RequiredPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredPositions
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
