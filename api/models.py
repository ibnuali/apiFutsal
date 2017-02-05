# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    id_room = models.ForeignKey('Room', models.DO_NOTHING, db_column='id_room', blank=True, null=True)
    id_friend = models.ForeignKey('Friend', models.DO_NOTHING, db_column='id_friend', blank=True, null=True)
    id_party = models.ForeignKey('Party', models.DO_NOTHING, db_column='id_party', blank=True, null=True)
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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Field(models.Model):
    id_field = models.AutoField(primary_key=True)
    name_field = models.CharField(max_length=30)
    latitude_field = models.FloatField()
    longitude_field = models.FloatField()
    description_field = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'field'


class FieldLocation(models.Model):
    id_field_location = models.AutoField(primary_key=True)
    id_district = models.ForeignKey(District, models.DO_NOTHING, db_column='id_district')
    name_field_location = models.CharField(max_length=40)
    latitude_field_location = models.FloatField()
    longitude_field_location = models.FloatField()

    class Meta:
        managed = False
        db_table = 'field_location'


class FieldPhotos(models.Model):
    id_field = models.ForeignKey(Field, models.DO_NOTHING, db_column='id_field', primary_key=True)
    field_photos = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'field_photos'


class Friend(models.Model):
    id_friend = models.AutoField(primary_key=True)
    id_player1 = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player1', related_name="id_player1")
    id_player2 = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player2', related_name="id_player2")
    friend_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friend'


class Genders(models.Model):
    id_gender = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'genders'


class JoinParty(models.Model):
    id_join_party = models.AutoField(primary_key=True)
    id_party = models.ForeignKey('Party', models.DO_NOTHING, db_column='id_party')
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    date_join_party = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'join_party'


class JoinRoom(models.Model):
    id_join_room = models.AutoField(primary_key=True)
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    id_room = models.ForeignKey('Room', models.DO_NOTHING, db_column='id_room')
    date_join_room = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'join_room'


class Level(models.Model):
    id_level = models.AutoField(primary_key=True)
    score_level = models.IntegerField()
    score_exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'level'


class LevelHistory(models.Model):
    id_level_history = models.IntegerField(primary_key=True)
    id_level = models.ForeignKey(Level, models.DO_NOTHING, db_column='id_level')
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    date_level_history = models.DateTimeField()
    player_exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'level_history'


class Party(models.Model):
    id_party = models.AutoField(primary_key=True)
    id_player = models.ForeignKey('Player', models.DO_NOTHING, db_column='id_player')
    party_name = models.CharField(max_length=50)
    party_created = models.DateTimeField()
    party_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party'


class Player(models.Model):
    id_player = models.AutoField(primary_key=True)
    id_district = models.ForeignKey(District, models.DO_NOTHING, db_column='id_district', blank=True, null=True)
    id_gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='id_gender')
    player_first_name = models.CharField(max_length=20)
    player_last_name = models.CharField(max_length=20)
    player_photo = models.CharField(max_length=30)
    player_birth_place = models.CharField(max_length=30)
    player_birth_date = models.DateField()
    player_address = models.CharField(max_length=80, blank=True, null=True)
    player_handphone = models.CharField(max_length=13)
    player_email = models.CharField(max_length=50)
    player_username = models.CharField(max_length=30)
    player_password = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class PlayerPosition(models.Model):
    id_player_position = models.AutoField(primary_key=True)
    id_position = models.ForeignKey('Positions', models.DO_NOTHING, db_column='id_position')
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player')

    class Meta:
        managed = False
        db_table = 'player_position'


class Positions(models.Model):
    id_position = models.AutoField(primary_key=True)
    position = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'positions'


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


class RatingHistory(models.Model):
    id_rating_history = models.AutoField(primary_key=True)
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player')
    id_rating = models.ForeignKey(Rating, models.DO_NOTHING, db_column='id_rating')
    date_rating_history = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rating_history'


class RequiredPositions(models.Model):
    id_required_positions = models.AutoField(primary_key=True)
    id_room = models.ForeignKey('Room', models.DO_NOTHING, db_column='id_room')
    id_position = models.ForeignKey(Positions, models.DO_NOTHING, db_column='id_position')

    class Meta:
        managed = False
        db_table = 'required_positions'


class Room(models.Model):
    id_room = models.AutoField(primary_key=True)
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player')
    required_gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='required_gender', blank=True, null=True)
    id_field_location = models.ForeignKey(FieldLocation, models.DO_NOTHING, db_column='id_field_location', blank=True, null=True)
    room_name = models.CharField(max_length=50)
    room_stadium = models.CharField(max_length=40)
    room_address = models.CharField(max_length=80)
    room_date = models.DateTimeField()
    room_duration = models.TimeField()
    required_level_min = models.IntegerField(blank=True, null=True)
    required_level_max = models.IntegerField(blank=True, null=True)
    required_age_min = models.IntegerField(blank=True, null=True)
    required_age_max = models.IntegerField(blank=True, null=True)
    required_slot = models.IntegerField()
    room_status = models.IntegerField()
    room_created = models.DateTimeField()
    room_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Store(models.Model):
    id_store = models.AutoField(primary_key=True)
    name_store = models.CharField(max_length=40)
    description_store = models.CharField(max_length=100)
    contact_store = models.CharField(max_length=14)
    link_store = models.CharField(max_length=40)
    photo_store = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'store'
