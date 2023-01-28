create database IF not exists net_elder;
create table url
(
    `id` int(11) not null AUTO_INCREMENT PRIMARY KEY ,
    `url` varchar(200) NOT NULL default 'default.url',
    `title` varchar(200) default 'default title',
    `description` varchar(200) default 'default description',
    `create_time` timestamp NOT NULL default CURRENT_TIMESTAMP
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
