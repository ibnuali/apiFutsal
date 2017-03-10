# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.db.models import Count


class Adds(models.Model):
    id_adds = models.AutoField(primary_key=True)
    adds_name = models.CharField(max_length=60)
    adds_seller = models.CharField(max_length=40)
    adds_description = models.CharField(max_length=60)
    adds_photo = models.CharField(max_length=30)
    add_url = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adds'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    id_room = models.ForeignKey('Room', models.DO_NOTHING, db_column='id_room', blank=True, null=True)
    id_friend = models.ForeignKey('Friend', models.DO_NOTHING, db_column='id_friend', blank=True, null=True)
    id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='id_team', blank=True, null=True)
    chat_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat'


class City(models.Model):
    id_city = models.CharField(primary_key=True, max_length=4)
    id_province = models.ForeignKey('Province', models.DO_NOTHING, db_column='id_province')
    name_city = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'city'


class Coin(models.Model):
    id_coin = models.AutoField(primary_key=True)
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player', blank=True, null=True)
    date_coin_history = models.DateTimeField()
    coin_change = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coin'


class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    name_country = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'country'


class District(models.Model):
    id_district = models.CharField(primary_key=True, max_length=7)
    id_city = models.ForeignKey(City, models.DO_NOTHING, db_column='id_city')
    name_district = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'district'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExpertJudgement(models.Model):
    id_expert_judgement = models.CharField(primary_key=True, max_length=9)
    name_expert_judgement = models.CharField(max_length=30)
    birth_day_expert_judgement = models.DateTimeField()
    birth_place_expert_judgement = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'expert_judgement'


class Friend(models.Model):
    id_friend = models.AutoField(primary_key=True)
    id_player1 = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player1',related_name='player1')
    id_player2 = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player2',related_name='player2')

    class Meta:
        managed = False
        db_table = 'friend'


class Genders(models.Model):
    gender = models.CharField(primary_key=True, max_length=6)

    class Meta:
        managed = False
        db_table = 'genders'


class JoinRoom(models.Model):
    id_join_room = models.AutoField(primary_key=True)
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    id_room = models.ForeignKey('Room', models.DO_NOTHING, db_column='id_room')
    date_join_room = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'join_room'


class JoinTeam(models.Model):
    id_join_team = models.AutoField(primary_key=True)
    id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='id_team')
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    date_join_team = models.DateTimeField()
    join_team_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'join_team'


class JoinTournament(models.Model):
    id_join_tournament = models.AutoField(primary_key=True)
    id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='id_team')
    id_tournament = models.ForeignKey('Tournament', models.DO_NOTHING, db_column='id_tournament')
    join_tournament_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'join_tournament'


class Level(models.Model):
    id_level = models.AutoField(primary_key=True)
    name_category = models.ForeignKey('LevelCategory', models.DO_NOTHING, db_column='name_category', blank=True, null=True)
    score_level = models.IntegerField()
    score_exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'level'


class LevelCategory(models.Model):
    name_category = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'level_category'


class LevelHistory(models.Model):
    id_level_history = models.IntegerField(primary_key=True)
    id_level = models.ForeignKey(Level, models.DO_NOTHING, db_column='id_level')
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    date_level_history = models.DateTimeField()
    player_exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'level_history'


class LineUp(models.Model):
    id_line_up = models.AutoField(primary_key=True)
    line_up_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'line_up'


class LineUpPlayer(models.Model):
    id_join_team = models.ForeignKey(JoinTeam, models.DO_NOTHING, db_column='id_join_team')
    id_line_up = models.ForeignKey(LineUp, models.DO_NOTHING, db_column='id_line_up')
    line_up_player_goal = models.IntegerField(blank=True, null=True)
    line_up_player_intercept = models.IntegerField(blank=True, null=True)
    line_up_player_save = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'line_up_player'
        unique_together = (('id_join_team', 'id_line_up'),)


class MatchTeam(models.Model):
    id_match_team = models.AutoField(primary_key=True)
    id_line_up = models.ForeignKey(LineUp, models.DO_NOTHING, db_column='id_line_up')
    id_play_match = models.ForeignKey('PlayMatch', models.DO_NOTHING, db_column='id_play_match')
    match_team_final_score = models.IntegerField()
    match_team_status = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'match_team'


class OfficialTeam(models.Model):
    id_official_team = models.AutoField(primary_key=True)
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='id_team')
    date_official_team = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'official_team'


class OfficialTournament(models.Model):
    id_official_tournament = models.AutoField(primary_key=True)
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    id_tournament = models.ForeignKey('Tournament', models.DO_NOTHING, db_column='id_tournament')
    official_tournament_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'official_tournament'


class OpenMatch(models.Model):
    id_open_match = models.AutoField(primary_key=True)
    id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='id_team')
    id_city = models.ForeignKey(City, models.DO_NOTHING, db_column='id_city', blank=True, null=True)
    id_play_match = models.ForeignKey('PlayMatch', models.DO_NOTHING, db_column='id_play_match', blank=True, null=True)
    open_match_date = models.DateField(blank=True, null=True)
    open_match_location = models.CharField(max_length=50, blank=True, null=True)
    open_match_created = models.DateTimeField()
    open_match_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_match'


class PlayMatch(models.Model):
    id_play_match = models.AutoField(primary_key=True)
    id_tournament = models.ForeignKey('Tournament', models.DO_NOTHING, db_column='id_tournament', blank=True, null=True)
    id_open_match = models.ForeignKey(OpenMatch, models.DO_NOTHING, db_column='id_open_match', blank=True, null=True)
    id_city = models.ForeignKey(City, models.DO_NOTHING, db_column='id_city')
    play_match_date = models.DateField()
    play_match_place = models.CharField(max_length=40)
    play_match_duration = models.TimeField()

    class Meta:
        managed = False
        db_table = 'play_match'


class Player(models.Model):
    id_player = models.AutoField(primary_key=True)
    id_district = models.CharField(max_length=7, blank=True, null=True)
    gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='gender')
    player_first_name = models.CharField(max_length=20)
    player_last_name = models.CharField(max_length=20)
    player_nick_name = models.CharField(max_length=12)
    player_photo = models.CharField(max_length=30)
    player_birth_place = models.CharField(max_length=30, blank=True, null=True)
    player_birth_date = models.DateField(blank=True, null=True)
    player_address = models.CharField(max_length=80, blank=True, null=True)
    player_handphone = models.CharField(max_length=13)
    player_email = models.CharField(max_length=50)
    player_username = models.CharField(max_length=30)
    player_password = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    #Method untuk ngambil data level seorang pemain
    def __player_level(self):
        level_hist = LevelHistory.objects.raw('''SELECT *
                                              FROM level_history lh
                                              INNER JOIN (
                                              SELECT l.score_level,MAX(date_level_history) AS MaxDate
                                              FROM level_history lm
                                              INNER JOIN (
                                              SELECT *
                                              FROM level) l
                                              ON l.id_level = lm.id_level
                                              AND lm.id_player = %s
                                              ) lm ON lh.id_player = %s AND lh.date_level_history = lm.MaxDate''',[self.id_player,self.id_player])
        if not sum(1 for level in level_hist):
            return 0
        else:
            return level_hist[0].score_level

    #Method untuk ngambil data exp seorang pemain
    def __player_exp(self):
        level_hist = LevelHistory.objects.raw('''SELECT *
                                              FROM level_history lh
                                              INNER JOIN (
                                              SELECT l.score_level,MAX(date_level_history) AS MaxDate
                                              FROM level_history lm
                                              INNER JOIN (
                                              SELECT *
                                              FROM level) l
                                              ON l.id_level = lm.id_level
                                              AND lm.id_player = %s
                                              ) lm ON lh.id_player = %s AND lh.date_level_history = lm.MaxDate LIMIT 1''',[self.id_player,self.id_player])

        if not sum(1 for level in level_hist):
            return 0
        else:
            return level_hist[0].player_exp

    #Method untuk ngambil data rating seorang pemain
    def __player_rating(self):
        rating_hist = RatingHistory.objects.raw('''
            SELECT *,SUM(r.score_rating) as score, COUNT(rh.id_rating_history) as review, rh.short_rating_category
                                              FROM rating_history rh, rating r,rating_category rc
                                              WHERE rh.id_rating = %s AND rh.short_rating_category = rc.short_rating_category GROUP BY rc.short_rating_category
                                              ''',[self.id_player])


        if not sum(1 for rating in rating_hist):
            return 0
        else:
            return rating_hist[0]
    #Method untuk ngambil data total orang yang meriview seorang pemain
    def __player_reviewed(self):
        rating_hist = RatingHistory.objects.filter(id_player = self.id_player).aggregate(Count('id_rating_history'))
        return rating_hist["id_rating_history__count"]

    #Method untuk ngambil data posisi seorang pemain
    def __player_positions(self):
        in_query = PlayerPosition.objects.filter(id_player = self.id_player).values('short_position')
        positions = Positions.objects.filter(short_position__in = in_query)
        return positions

    #Method untuk ngambil data rooms dimana pemain tersebut menjadi admin di room tersebut
    def __player_rooms(self):
        rooms = Room.objects.filter(id_player = self.id_player)
        return rooms

    #Method untuk ngambil data rooms dimana pemain tersebut bergabung di room tersebut
    def __player_join_rooms(self):
        join_rooms = JoinRoom.objects.filter(id_player = self.id_player)
        return join_rooms

    #Method untuk ngambil data teman dari seorang pemain
    def __player_friends(self):
        friend = Friend.objects.filter(id_player1 = self.id_player)
        return friend

    #definisi properti dan method yang ditampungnya
    player_level = property(__player_level)
    player_exp = property(__player_exp)
    player_rating = property(__player_rating)
    player_reviewed = property(__player_reviewed)
    player_positions = property(__player_positions)
    player_join_rooms = property(__player_join_rooms)
    player_rooms = property(__player_rooms)
    player_friends = property(__player_friends)

    def SignIn(username, password):
        queryset = Player.objects.filter(player_username=username).filter(player_password=password)
        return queryset


    class Meta:
        managed = False
        db_table = 'player'

class PlayerAchievement(models.Model):
    id_player_achievement = models.AutoField(primary_key=True)
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player')
    id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='id_team', blank=True, null=True)
    id_tournament = models.ForeignKey('Tournament', models.DO_NOTHING, db_column='id_tournament', blank=True, null=True)
    name_player_achievement = models.CharField(max_length=60)
    name_event_player_achievement = models.CharField(max_length=70, blank=True, null=True)
    date_player_achievement = models.DateField()
    with_team_player_achievement = models.CharField(max_length=40, blank=True, null=True)
    photo_prove_player_achievement = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'player_achievement'


class PlayerPosition(models.Model):
    id_player_position = models.AutoField(primary_key=True)
    short_position = models.ForeignKey('Positions', models.DO_NOTHING, db_column='short_position')
    id_player = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_position'


class Positions(models.Model):
    short_position = models.CharField(primary_key=True, max_length=5)
    long_position = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'positions'


class Promo(models.Model):
    id_promo = models.AutoField(primary_key=True)
    promo_name = models.CharField(max_length=60)
    promo_seller = models.CharField(max_length=40)
    promo_description = models.CharField(max_length=60)
    promo_photo = models.CharField(max_length=30)
    promo_seller_url = models.CharField(max_length=30, blank=True, null=True)
    promo_coin_required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promo'


class PromoCupon(models.Model):
    id_promo = models.ForeignKey(Promo, models.DO_NOTHING, db_column='id_promo')
    promo_cupon_code = models.CharField(primary_key=True, max_length=20)
    promo_cupon_image = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'promo_cupon'


class PromoHistory(models.Model):
    id_promo_history = models.AutoField(primary_key=True)
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player')
    promo_cupon_code = models.ForeignKey(PromoCupon, models.DO_NOTHING, db_column='promo_cupon_code')
    date_promo_history = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promo_history'


class Province(models.Model):
    id_province = models.CharField(primary_key=True, max_length=2)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country')
    name_province = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'province'


class Rating(models.Model):
    id_rating = models.AutoField(primary_key=True)
    score_rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rating'


class RatingCategory(models.Model):
    short_rating_category = models.CharField(primary_key=True, max_length=7)
    long_rating_category = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'rating_category'


class RatingHistory(models.Model):
    id_rating_history = models.AutoField(primary_key=True)
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player',related_name='id_playerRating')
    player_give_rating = models.ForeignKey(Player, models.DO_NOTHING, db_column='player_give_rating',related_name='player_give_rating')
    id_expert_judgement = models.ForeignKey(ExpertJudgement, models.DO_NOTHING, db_column='id_expert_judgement', blank=True, null=True)
    short_rating_category = models.ForeignKey(RatingCategory, models.DO_NOTHING, db_column='short_rating_category')
    id_rating = models.ForeignKey(Rating, models.DO_NOTHING, db_column='id_rating')
    date_rating_history = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rating_history'


class RequiredPositions(models.Model):
    id_required_positions = models.AutoField(primary_key=True)
    id_room = models.ForeignKey('Room', models.DO_NOTHING, db_column='id_room')
    short_position = models.ForeignKey(Positions, models.DO_NOTHING, db_column='short_position')

    class Meta:
        managed = False
        db_table = 'required_positions'


class Room(models.Model):
    id_room = models.AutoField(primary_key=True)
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player')
    required_gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='required_gender', blank=True, null=True)
    id_city = models.ForeignKey(City, models.DO_NOTHING, db_column='id_city', blank=True, null=True)
    room_name = models.CharField(max_length=50)
    room_stadium = models.CharField(max_length=40)
    room_address = models.CharField(max_length=80)
    room_share_location = models.CharField(max_length=20, blank=True, null=True)
    room_date = models.DateTimeField()
    room_duration = models.TimeField()
    required_level_min = models.IntegerField(blank=True, null=True)
    required_level_max = models.IntegerField(blank=True, null=True)
    required_age_min = models.IntegerField(blank=True, null=True)
    required_age_max = models.IntegerField(blank=True, null=True)
    required_slot = models.IntegerField()
    room_password = models.CharField(max_length=50, blank=True, null=True)
    room_status = models.IntegerField()
    room_created = models.DateTimeField()
    room_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Team(models.Model):
    id_team = models.AutoField(primary_key=True)
    id_city = models.ForeignKey(City, models.DO_NOTHING, db_column='id_city')
    team_name = models.CharField(max_length=50)
    team_logo = models.CharField(max_length=30)
    team_established = models.DateField()
    team_created = models.DateTimeField()
    team_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'


class TeamAchievement(models.Model):
    id_team_achievement = models.IntegerField(primary_key=True)
    id_team = models.ForeignKey(Team, models.DO_NOTHING, db_column='id_team')
    name_team_achievement = models.CharField(max_length=60)
    event_team_achievement = models.CharField(max_length=50, blank=True, null=True)
    id_tournament = models.ForeignKey('Tournament', models.DO_NOTHING, db_column='id_tournament', blank=True, null=True)
    date_team_achievement = models.DateField()

    class Meta:
        managed = False
        db_table = 'team_achievement'


class Tournament(models.Model):
    id_tournament = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=30)
    tournament_official_name = models.CharField(max_length=40)
    tournament_city = models.ForeignKey(City, models.DO_NOTHING, db_column='tournament_city')
    tournament_address = models.CharField(max_length=50)
    tournament_start_date = models.DateField()
    tournament_finish_date = models.DateField()
    tournament_type = models.CharField(max_length=6)
    tournament_member = models.IntegerField()
    tournament_required_play = models.IntegerField(blank=True, null=True)
    tournament_required_win = models.IntegerField(blank=True, null=True)
    tournament_password = models.CharField(max_length=20)
    tournament_created_at = models.DateTimeField()
    tournament_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournament'


class TransferCoin(models.Model):
    id_transfer_coin = models.AutoField(primary_key=True)
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player', blank=True, null=True,related_name='id_playerTransferCoin')
    id_player_transfered = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player_transfered', blank=True, null=True,related_name='id_playerTransferd')
    date_transfer_coin = models.DateTimeField()
    coin_transfered = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transfer_coin'
