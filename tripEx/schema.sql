/*
later ip1,2,interest,tripstyle-> change to integer
using join
*/
create table if not exists user (
    userNum integer primary key autoincrement,
    name string not null,
    email string not null,
    address string not null,
    interestedPlace1 string not null,
    interestedPlace2 string not null,
    profilepic blob,
    userID string not null,
    password string not null,
    interest string not null,
    tripstyle string not null,
    pubTime integer not null
);

create table if not exists distriction (
    districtionNum integer primary key,
    districtionName string not null
);

create table if not exists posting (
    postingNum integer primary key autoincrement,
    title string not null,
    userNum integer not null,
    contents string not null,
    tripdate integer,
    destination1 integer,
    destination2 integer,
    pubTime integer not null
);

create table if not exists reply (
    replyNum integer primary key autoincrement,
    replyerID string not null,
    replytitle string not null,
    replycontents string not null
);

create table if not exists nation (
    nationNum integer primary key,
    nationName string not null
);

create table if not exists style (
    styleNum integer primary key,
    styleContent string not null
);

create table if not exists follower (
    who_num integer,
    whom_num integer
);