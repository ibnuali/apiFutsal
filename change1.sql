ALTER TABLE `player_position` ADD INDEX(`id_player`);
ALTER TABLE `player_position` ADD CONSTRAINT `FK_player_player_position_fk` FOREIGN KEY (`id_player`) REFERENCES `db_futsal`.`player`(`id_player`) ON DELETE RESTRICT ON UPDATE RESTRICT;
DROP TABLE `official_team`;
ALTER TABLE `team` CHANGE `team_logo` `team_logo` VARCHAR(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'urldefault';
ALTER TABLE  `join_team` CHANGE  `join_team_status`  `official_team_status` INT( 11 ) NOT NULL DEFAULT  '0';
ALTER TABLE  `join_team` ADD  `date_official_team` DATETIME NOT NULL ;
