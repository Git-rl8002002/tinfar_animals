/*
* Author   : JasonHung
* Date     : 20221129
* Update   : 20221129
* Function : new taipei animals
*/

/*
 * database  tinfar_medicine
 */ 
create database tinfar_animals DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
use tinfar_animals;
/* 
 * setup_record
 */
create table setup_record(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
a_user varchar(50) null,
s_id varchar(20) null,
s_item varchar(50) null,
s_position varchar(50) null,
s_ip varchar(50) null,
s_area varchar(50) null,
s_alarm_top varchar(50) null,
s_alarm_bottom varchar(50) null,
s_top_auto_run varchar(30) null,
s_top_manual_run varchar(50) null,
s_bottom_auto_run varchar(30) null,
s_bottom_manual_run varchar(50) null,
s_alarm_top_device varchar(70) null,
s_alarm_bottom_device varchar(70) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('1', 'temp' ,'a' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('1', 'temp' ,'a' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('1', 'rh'   ,'a' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('1', 'rh'   ,'a' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('1', 'nh3'  ,'a' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('1', 'nh3'  ,'a' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('1', 'h2s'  ,'a' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('1', 'h2s'  ,'a' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('1', 'pr'   ,'a' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('1', 'pr'   ,'a' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('2', 'temp' ,'a' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('2', 'temp' ,'a' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('2', 'rh'   ,'a' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('2', 'rh'   ,'a' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('2', 'nh3'  ,'a' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('2', 'nh3'  ,'a' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('2', 'h2s'  ,'a' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('2', 'h2s'  ,'a' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('2', 'pr'   ,'a' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('2', 'pr'   ,'a' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('3', 'temp' ,'a' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('3', 'temp' ,'a' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('3', 'rh'   ,'a' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('3', 'rh'   ,'a' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('3', 'nh3'  ,'a' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('3', 'nh3'  ,'a' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('3', 'h2s'  ,'a' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('3', 'h2s'  ,'a' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('3', 'pr'   ,'a' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('3', 'pr'   ,'a' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('4', 'temp' ,'a' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('4', 'temp' ,'a' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('4', 'rh'   ,'a' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('4', 'rh'   ,'a' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('4', 'nh3'  ,'a' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('4', 'nh3'  ,'a' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('4', 'h2s'  ,'a' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('4', 'h2s'  ,'a' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('4', 'pr'   ,'a' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('4', 'pr'   ,'a' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('5', 'temp' ,'b' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('5', 'temp' ,'b' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('5', 'rh'   ,'b' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('5', 'rh'   ,'b' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('5', 'nh3'  ,'b' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('5', 'nh3'  ,'b' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('5', 'h2s'  ,'b' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('5', 'h2s'  ,'b' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('5', 'pr'   ,'b' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('5', 'pr'   ,'b' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('6', 'temp' ,'b' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('6', 'temp' ,'b' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('6', 'rh'   ,'b' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('6', 'rh'   ,'b' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('6', 'nh3'  ,'b' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('6', 'nh3'  ,'b' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('6', 'h2s'  ,'b' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('6', 'h2s'  ,'b' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('6', 'pr'   ,'b' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('6', 'pr'   ,'b' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('7', 'temp' ,'b' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('7', 'temp' ,'b' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('7', 'rh'   ,'b' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('7', 'rh'   ,'b' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('7', 'nh3'  ,'b' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('7', 'nh3'  ,'b' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('7', 'h2s'  ,'b' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('7', 'h2s'  ,'b' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('7', 'pr'   ,'b' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('7', 'pr'   ,'b' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('8', 'temp' ,'c' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('8', 'temp' ,'c' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('8', 'rh'   ,'c' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('8', 'rh'   ,'c' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('8', 'nh3'  ,'c' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('8', 'nh3'  ,'c' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('8', 'h2s'  ,'c' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('8', 'h2s'  ,'c' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('8', 'pr'   ,'c' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('8', 'pr'   ,'c' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('9', 'temp' ,'c' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('9', 'temp' ,'c' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('9', 'rh'   ,'c' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('9', 'rh'   ,'c' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('9', 'nh3'  ,'c' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('9', 'nh3'  ,'c' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('9', 'h2s'  ,'c' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('9', 'h2s'  ,'c' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('9', 'pr'   ,'c' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('9', 'pr'   ,'c' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('10', 'temp' ,'c' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('10', 'temp' ,'c' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('10', 'rh'   ,'c' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('10', 'rh'   ,'c' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('10', 'nh3'  ,'c' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('10', 'nh3'  ,'c' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('10', 'h2s'  ,'c' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('10', 'h2s'  ,'c' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('10', 'pr'   ,'c' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('10', 'pr'   ,'c' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('11', 'temp' ,'c' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('11', 'temp' ,'c' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('11', 'rh'   ,'c' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('11', 'rh'   ,'c' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('11', 'nh3'  ,'c' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('11', 'nh3'  ,'c' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('11', 'h2s'  ,'c' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('11', 'h2s'  ,'c' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('11', 'pr'   ,'c' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('11', 'pr'   ,'c' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('12', 'temp' ,'c' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('12', 'temp' ,'c' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('12', 'rh'   ,'c' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('12', 'rh'   ,'c' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('12', 'nh3'  ,'c' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('12', 'nh3'  ,'c' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('12', 'h2s'  ,'c' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('12', 'h2s'  ,'c' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('12', 'pr'   ,'c' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('12', 'pr'   ,'c' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('13', 'temp' ,'d' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('13', 'temp' ,'d' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('13', 'rh'   ,'d' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('13', 'rh'   ,'d' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('13', 'nh3'  ,'d' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('13', 'nh3'  ,'d' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('13', 'h2s'  ,'d' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('13', 'h2s'  ,'d' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('13', 'pr'   ,'d' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('13', 'pr'   ,'d' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('14', 'temp' ,'d' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('14', 'temp' ,'d' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('14', 'rh'   ,'d' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('14', 'rh'   ,'d' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('14', 'nh3'  ,'d' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('14', 'nh3'  ,'d' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('14', 'h2s'  ,'d' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('14', 'h2s'  ,'d' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('14', 'pr'   ,'d' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('14', 'pr'   ,'d' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('15', 'temp' ,'d' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('15', 'temp' ,'d' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('15', 'rh'   ,'d' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('15', 'rh'   ,'d' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('15', 'nh3'  ,'d' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('15', 'nh3'  ,'d' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('15', 'h2s'  ,'d' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('15', 'h2s'  ,'d' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('15', 'pr'   ,'d' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('15', 'pr'   ,'d' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('16', 'temp' ,'d' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('16', 'temp' ,'d' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('16', 'rh'   ,'d' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('16', 'rh'   ,'d' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('16', 'nh3'  ,'d' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('16', 'nh3'  ,'d' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('16', 'h2s'  ,'d' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('16', 'h2s'  ,'d' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('16', 'pr'   ,'d' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('16', 'pr'   ,'d' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('17', 'temp' ,'e' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('17', 'temp' ,'e' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('17', 'rh'   ,'e' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('17', 'rh'   ,'e' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('17', 'nh3'  ,'e' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('17', 'nh3'  ,'e' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('17', 'h2s'  ,'e' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('17', 'h2s'  ,'e' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('17', 'pr'   ,'e' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('17', 'pr'   ,'e' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('18', 'temp' ,'e' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('18', 'temp' ,'e' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('18', 'rh'   ,'e' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('18', 'rh'   ,'e' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('18', 'nh3'  ,'e' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('18', 'nh3'  ,'e' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('18', 'h2s'  ,'e' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('18', 'h2s'  ,'e' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('18', 'pr'   ,'e' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('18', 'pr'   ,'e' , 'bottom' , '1050' , '排風扇' , 'enable');

insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('19', 'temp' ,'e' , 'top'    , '30'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('19', 'temp' ,'e' , 'bottom' , '18'   , '加熱燈' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('19', 'rh'   ,'e' , 'top'    , '60'   , '除濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('19', 'rh'   ,'e' , 'bottom' , '30'   , '加濕機' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('19', 'nh3'  ,'e' , 'top'    , '50'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('19', 'nh3'  ,'e' , 'bottom' , '20'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('19', 'h2s'  ,'e' , 'top'    , '10'   , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('19', 'h2s'  ,'e' , 'bottom' , '5'    , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_top , s_alarm_top_device , s_top_auto_run)          value('19', 'pr'   ,'e' , 'top'    , '1100' , '排風扇' , 'enable');
insert into `setup_record`(s_id , s_item , s_area , s_position , s_alarm_bottom , s_alarm_bottom_device , s_bottom_auto_run) value('19', 'pr'   ,'e' , 'bottom' , '1050' , '排風扇' , 'enable');

/* 
 * history_record
 */
create table history_record(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
a_user varchar(50) null,
o_item text null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * work_record
 */
create table work_record(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
r_year varchar(50) null,
r_month varchar(50) null,
r_day varchar(50) null,
a_user varchar(50) null,
o_item text null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * sensor
 */
create table sensor(
no int not null primary key AUTO_INCREMENT,r_time datetime null,
r_year varchar(100) null,
r_month varchar(100) null,
r_day varchar(100) null,
s_area varchar(200) null,
s_kind varchar(200) null,
s_content varchar(200) null,
s_protocol varchar(200) null,
val_1 varchar(200) null,
val_2 varchar(200) null,
val_3 varchar(200) null,
val_4 varchar(200) null,
val_5 varchar(200) null,
r_status varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;



/* 
 * in_out_record
 */
create table in_out_record(
no int not null primary key AUTO_INCREMENT,
login_time datetime null,
logout_time datetime null,
login_code varchar(200) null,
r_year varchar(100) null,
r_month varchar(100) null,
r_day varchar(100) null,
a_user varchar(200) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * account
 */
create table account(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
r_year varchar(100) null,
r_month varchar(100) null,
r_day varchar(100) null,
a_user varchar(200) null,
a_pwd varchar(200) null,
a_lv varchar(10) null,
a_status varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into account(a_user , a_pwd , a_lv , a_status) value('admin','1qaz','1','run');

