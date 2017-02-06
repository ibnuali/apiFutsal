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

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('id_district','player_photo','player_address','created_at','updated_at')

class PlayerPositionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    player_gender = GenderSerializer(read_only=True,source='id_gender')
    player_positions = PlayerPositionListSerializer(many=True,read_only=True)
    class Meta:
        model = Player
        fields = ('id_player','player_first_name','player_last_name','player_gender',
        'player_photo','player_level','player_exp','player_rating','player_reviewed','player_positions',)

class PlayerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('created_at','updated_at')

class ChatFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        exclude = ('id_player','id_room','id_party')

class PlayerFriendListSerializer(serializers.ModelSerializer):
    id_player2 = PlayerSerializer(read_only=True)
    chat = ChatFriendSerializer(many=True,read_only=True)
    class Meta:
        model = Friend
        exclude = ('id_player1',)

class PlayerRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id_field_location','room_name','room_stadium',
                    'room_address','room_duration','room_date')

class PlayerJoinRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRoom
        exclude = ('id_player')

class PlayerDetailSerializer(serializers.ModelSerializer):
    player_gender = GenderSerializer(read_only=True,source='id_gender')
    player_level = serializers.IntegerField(read_only=True)
    player_exp = serializers.IntegerField(read_only=True)
    player_rating = serializers.IntegerField(read_only=True)
    player_reviewed = serializers.IntegerField(read_only=True)
    player_friends = PlayerFriendListSerializer(many=True,read_only=True)
    player_rooms = PlayerRoomSerializer(many=True,read_only=True)
    player_join_rooms = PlayerJoinRoomSerializer(many=True,read_only=True)
    player_positions = PlayerPositionListSerializer(many=True,read_only=True)
    class Meta:
        model = Player
        fields = ('id_player','player_first_name','player_last_name','player_gender','player_photo',
        'player_birth_place','player_birth_date','player_address','id_district','player_handphone',
        'player_email','player_username','player_level','player_exp','player_rating','player_reviewed','player_positions',
        'player_rooms','player_join_rooms','player_friends')

class RoomSerializer(serializers.ModelSerializer):
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


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
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
