create table usertable(
userNum int not null auto_increment primary key,
name varchar(50) not null,
email varchar(100) not null,
address varchar(200) not null,
interestedPlace1 int,
intersetedPlace1 int,
profilepic blob,
userID varchar(100) not null,
password varchar(100) not null,
interested varchar(100),
style int,
createdTime datetime
);

describe usertable;

alter table usertable modify createdTime datetime not null;

alter table usertable convert to character set utf8;