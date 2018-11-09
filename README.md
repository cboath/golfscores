# golfscores

Postgres table creation

create table courses (
course_id SERIAL not null primary key,
course_name varchar not null
);

create table players (
player_id serial not null primary key,
first_name varchar not null,
last_name varchar not null,
handicap int
);

insert into players (first_name, last_name, handicap) values ('Chris', 'Teater', 16);
insert into courses (course_name) values ('Eagle Springs');
