/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     1/27/2017 10:04:52 AM                        */
/*==============================================================*/


drop table if exists chat;

drop table if exists city;

drop table if exists country;

drop table if exists district;

drop table if exists field;

drop table if exists field_location;

drop table if exists field_photos;

drop table if exists friend;

drop table if exists genders;

drop table if exists join_party;

drop table if exists join_room;

drop table if exists level;

drop table if exists level_history;

drop table if exists party;

drop table if exists player;

drop table if exists player_position;

drop table if exists positions;

drop table if exists province;

drop table if exists rating;

drop table if exists rating_history;

drop table if exists required_positions;

drop table if exists room;

drop table if exists store;

/*==============================================================*/
/* Table: chat                                                  */
/*==============================================================*/
create table chat
(
   id_chat              int(11) not null auto_increment,
   id_player            int(11) not null,
   id_room              int(11),
   id_friend            int(11),
   id_party             int(11),
   chat_type            int,
   primary key (id_chat)
);

/*==============================================================*/
/* Table: city                                                  */
/*==============================================================*/
create table city
(
   id_city              varchar(4) not null,
   id_province          varchar(2) not null,
   name_city            varchar(50) not null,
   primary key (id_city)
);

/*==============================================================*/
/* Table: country                                               */
/*==============================================================*/
create table country
(
   id_country           int(11) not null auto_increment,
   name_country         varchar(40) not null,
   primary key (id_country)
);

/*==============================================================*/
/* Table: district                                              */
/*==============================================================*/
create table district
(
   id_district          varchar(7) not null,
   id_city              varchar(4) not null,
   name_district        varchar(60) not null,
   primary key (id_district)
);

/*==============================================================*/
/* Table: field                                                 */
/*==============================================================*/
create table field
(
   id_field             int not null auto_increment,
   name_field           varchar(30) not null,
   latitude_field       double not null,
   longitude_field      double not null,
   description_field    varchar(100) not null,
   primary key (id_field)
);

/*==============================================================*/
/* Table: field_location                                        */
/*==============================================================*/
create table field_location
(
   id_field_location    int(11) not null auto_increment,
   id_district          varchar(7) not null,
   name_field_location  varchar(40) not null,
   latitude_field_location double not null,
   longitude_field_location double not null,
   primary key (id_field_location)
);

/*==============================================================*/
/* Table: field_photos                                          */
/*==============================================================*/
create table field_photos
(
   id_field             int not null,
   field_photos         varchar(50) not null,
   primary key (id_field)
);

/*==============================================================*/
/* Table: friend                                                */
/*==============================================================*/
create table friend
(
   id_friend            int(11) not null auto_increment,
   id_player1           int(11) not null,
   id_player2           int(11) not null,
   friend_status        int,
   primary key (id_friend)
);

/*==============================================================*/
/* Table: genders                                               */
/*==============================================================*/
create table genders
(
   id_gender            int(11) not null auto_increment,
   gender               varchar(6) not null,
   primary key (id_gender)
);

/*==============================================================*/
/* Table: join_party                                            */
/*==============================================================*/
create table join_party
(
   id_join_party        int(11) not null auto_increment,
   id_party             int(11) not null,
   id_player            int(11) not null,
   date_join_party      datetime not null,
   primary key (id_join_party)
);

/*==============================================================*/
/* Table: join_room                                             */
/*==============================================================*/
create table join_room
(
   id_join_room         int(11) not null auto_increment,
   id_player            int(11) not null,
   id_room              int(11) not null,
   date_join_room       datetime not null,
   primary key (id_join_room)
);

/*==============================================================*/
/* Table: level                                                 */
/*==============================================================*/
create table level
(
   id_level             int(11) not null auto_increment,
   score_level          int not null,
   score_exp            int not null,
   primary key (id_level)
);

/*==============================================================*/
/* Table: level_history                                         */
/*==============================================================*/
create table level_history
(
   id_level_history     int not null,
   id_level             int(11) not null,
   id_player            int(11) not null,
   date_level_history   datetime not null,
   player_exp           int not null,
   primary key (id_level_history)
);

/*==============================================================*/
/* Table: party                                                 */
/*==============================================================*/
create table party
(
   id_party             int(11) not null auto_increment,
   id_player            int(11) not null,
   party_name           varchar(50) not null,
   party_created        datetime not null,
   party_status         int not null,
   primary key (id_party)
);

/*==============================================================*/
/* Table: player                                                */
/*==============================================================*/
create table player
(
   id_player            int(11) not null auto_increment,
   id_district          varchar(7),
   id_gender            int(11) not null,
   player_name          varchar(40) not null,
   player_photo         varchar(30) not null,
   player_birth_place   varchar(30) default NULL,
   player_birth_date    date default NULL,
   player_address       varchar(80) default NULL,
   player_handphone     varchar(13) not null,
   player_email         varchar(50) not null,
   player_username      varchar(30) not null,
   player_password      varchar(50) not null,
   created_at           datetime not null,
   updated_at           datetime default NULL,
   primary key (id_player)
);

/*==============================================================*/
/* Table: player_position                                       */
/*==============================================================*/
create table player_position
(
   id_player_position   int(11) not null auto_increment,
   id_position          int(11) not null,
   id_player            int(11) not null,
   primary key (id_player_position)
);

/*==============================================================*/
/* Table: positions                                             */
/*==============================================================*/
create table positions
(
   id_position          int(11) not null auto_increment,
   position             varchar(15) not null,
   primary key (id_position)
);

/*==============================================================*/
/* Table: province                                              */
/*==============================================================*/
create table province
(
   id_province          varchar(2) not null,
   id_country           int(11) not null,
   name_province        varchar(50) not null,
   primary key (id_province)
);

/*==============================================================*/
/* Table: rating                                                */
/*==============================================================*/
create table rating
(
   id_rating            int(11) not null auto_increment,
   score_rating         double not null,
   primary key (id_rating)
);

/*==============================================================*/
/* Table: rating_history                                        */
/*==============================================================*/
create table rating_history
(
   id_rating_history    int(11) not null auto_increment,
   id_player            int(11) not null,
   id_rating            int(11) not null,
   date_rating_history  datetime not null,
   primary key (id_rating_history)
);

/*==============================================================*/
/* Table: required_positions                                    */
/*==============================================================*/
create table required_positions
(
   id_required_positions int(11) not null auto_increment,
   id_room              int(11) not null,
   id_position          int(11) not null,
   primary key (id_required_positions)
);

/*==============================================================*/
/* Table: room                                                  */
/*==============================================================*/
create table room
(
   id_room              int(11) not null auto_increment,
   id_player            int(11) not null,
   required_gender      int(11),
   id_field_location    int(11),
   room_name            varchar(50) not null,
   room_stadium         varchar(40) not null,
   room_address         varchar(80) not null,
   room_date            datetime not null,
   room_duration        time not null,
   required_level_min   int default NULL,
   required_level_max   int default NULL,
   required_age_min     int default NULL,
   required_age_max     int default NULL,
   required_slot        int not null,
   room_status          int not null default 0,
   room_created         datetime not null,
   room_updated         datetime default NULL,
   primary key (id_room)
);

/*==============================================================*/
/* Table: store                                                 */
/*==============================================================*/
create table store
(
   id_store             int not null auto_increment,
   name_store           varchar(40) not null,
   description_store    varchar(100) not null,
   contact_store        varchar(14) not null,
   link_store           varchar(40) not null,
   photo_store          varchar(50) not null,
   primary key (id_store)
);

alter table chat add constraint FK_chat_friend foreign key (id_friend)
      references friend (id_friend) on delete restrict on update restrict;

alter table chat add constraint FK_chat_party foreign key (id_party)
      references party (id_party) on delete restrict on update restrict;

alter table chat add constraint FK_chat_room foreign key (id_room)
      references room (id_room) on delete restrict on update restrict;

alter table chat add constraint FK_player_chat_fk foreign key (id_player)
      references player (id_player) on delete restrict on update restrict;

alter table city add constraint FK_province_city_fk foreign key (id_province)
      references province (id_province) on delete restrict on update restrict;

alter table district add constraint FK_city_distict_fk foreign key (id_city)
      references city (id_city) on delete restrict on update restrict;

alter table field_location add constraint FK_district_field_fk foreign key (id_district)
      references district (id_district) on delete restrict on update restrict;

alter table field_photos add constraint FK_field_photos_fk foreign key (id_field)
      references field (id_field) on delete restrict on update restrict;

alter table friend add constraint FK_player_friend_fk1 foreign key (id_player2)
      references player (id_player) on delete restrict on update restrict;

alter table friend add constraint FK_player_friend_fk2 foreign key (id_player1)
      references player (id_player) on delete restrict on update restrict;

alter table join_party add constraint FK_party_join_party_fk foreign key (id_party)
      references party (id_party) on delete restrict on update restrict;

alter table join_party add constraint FK_player_join_party_fk foreign key (id_player)
      references player (id_player) on delete restrict on update restrict;

alter table join_room add constraint FK_player_join_room_fk foreign key (id_player)
      references player (id_player) on delete restrict on update restrict;

alter table join_room add constraint FK_room_join_room_fk foreign key (id_room)
      references room (id_room) on delete restrict on update restrict;

alter table level_history add constraint FK_level_level_history_fk foreign key (id_level)
      references level (id_level) on delete restrict on update restrict;

alter table level_history add constraint FK_player_level_history_fk foreign key (id_player)
      references player (id_player) on delete restrict on update restrict;

alter table party add constraint FK_party_master_fk foreign key (id_player)
      references player (id_player) on delete restrict on update restrict;

alter table player add constraint FK_distict_player_fk foreign key (id_district)
      references district (id_district) on delete restrict on update restrict;

alter table player add constraint FK_genders_player_fk foreign key (id_gender)
      references genders (id_gender) on delete restrict on update restrict;

alter table player_position add constraint FK_player_player_position_fk foreign key (id_player)
      references player (id_player) on delete restrict on update restrict;

alter table player_position add constraint FK_positions_player_position_fk foreign key (id_position)
      references positions (id_position) on delete restrict on update restrict;

alter table province add constraint FK_country_province_fk foreign key (id_country)
      references country (id_country) on delete restrict on update restrict;

alter table rating_history add constraint FK_player_rating_history_fk foreign key (id_player)
      references player (id_player) on delete restrict on update restrict;

alter table rating_history add constraint FK_rating_rating_history_fk foreign key (id_rating)
      references rating (id_rating) on delete restrict on update restrict;

alter table required_positions add constraint FK_positions_required_position_fk foreign key (id_position)
      references positions (id_position) on delete restrict on update restrict;

alter table required_positions add constraint FK_room_required_positions_fk foreign key (id_room)
      references room (id_room) on delete restrict on update restrict;

alter table room add constraint FK_distict_room_fk foreign key (id_field_location)
      references field_location (id_field_location) on delete restrict on update restrict;

alter table room add constraint FK_required_gender_fk foreign key (required_gender)
      references genders (id_gender) on delete restrict on update restrict;

alter table room add constraint FK_room_master_fk foreign key (id_player)
      references player (id_player) on delete restrict on update restrict;

