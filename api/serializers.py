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
        exclude = ('id_district','player_nick_name','created_at','updated_at')

class PlayerPositionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    player_gender = GenderSerializer(read_only=True,source='id_gender') #mengambil data gender dari pemain melalui GenderSerializer
    player_positions = PlayerPositionListSerializer(many=True,read_only=True) #mengambil data posisi dari pemain melalui PlayerPositionListSerializer
    class Meta:
        model = Player
        fields = ('id_player','player_first_name','player_last_name','player_username','player_gender','player_birth_place',
        'player_birth_date','player_photo','player_address','player_email','player_handphone',
        'player_level','player_exp','rating_byPlayer','rating_byExpert','player_positions',)

class PlayerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('created_at','updated_at')

class PlayerFriendDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id_player','player_first_name','player_last_name','player_username',
        'player_photo')

class PlayerFriendListSerializer(serializers.ModelSerializer):
    id_player2 = PlayerFriendDataSerializer(read_only=True) #Mengambil data teman seorang player melalui serializer PlayerFriendDataSerializer
    class Meta:
        model = Friend
        exclude = ('id_player1','friend_status')

class PlayerAchievementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerAchievement
        fields = ('id_player_achievement','name_event_player_achievement','date_player_achievement')

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ('id_city','team_established','team_created','team_update')

class PlayerTeamListSerializer(serializers.ModelSerializer):
    team = TeamListSerializer(read_only=True,source= 'id_team')
    class Meta:
        model = JoinTeam
        fields = ('id_join_team','team','official_team_status')

class PlayerScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class PlayerDetailSerializer(serializers.ModelSerializer):
    player_friends = PlayerFriendListSerializer(many=True,read_only=True)
    player_positions = PlayerPositionListSerializer(many=True,read_only=True)
    player_achievements = PlayerAchievementListSerializer(many=True,read_only=True)
    player_team = PlayerTeamListSerializer(many=True,read_only=True)
    player_schedule = PlayerScheduleSerializer(many=True,read_only=True)
    class Meta:
        model = Player
        fields = ('id_player','player_first_name','player_last_name','gender','player_photo',
        'player_birth_place','player_birth_date','player_address','id_district','player_handphone',
        'player_email','player_username','player_level','player_exp','player_positions'
        ,'player_friends','rating_byPlayer','rating_byExpert','player_achievements','player_team','player_schedule')

class PlayerRoomSerializer(serializers.ModelSerializer):
    player_positions = PlayerPositionListSerializer(many=True,read_only=True)
    class Meta:
        model = Player
        fields = ('id_player','player_first_name','player_last_name','player_photo','player_positions')

class CreateRoomSerializer(serializers.ModelSerializer):
    filled_slot = serializers.IntegerField()
    master_room = PlayerRoomSerializer(read_only=True,source='id_player') #Membuat properties master_room
    class Meta:
        model = Room
        exclude = ('room_status','id_player','room_created','room_updated')

class ListPlayerRoomSerializer(serializers.ModelSerializer):
    player = PlayerRoomSerializer(read_only=True,source='id_player')
    class Meta:
        model = JoinRoom
        fields = ('id_join_room','player','date_join_room')

class RoomDetailSerializer(serializers.ModelSerializer):
    room_players =  ListPlayerRoomSerializer(many=True,read_only=True)
    class Meta:
        model = Room
        exclude = ('room_status','room_created','room_updated')

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

class TeamSerializer(serializers.ModelSerializer):
    id_player = PlayerSerializer()
    class Meta:
        model = Team
        fields = '__all__'

class JoinTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinTeam
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
