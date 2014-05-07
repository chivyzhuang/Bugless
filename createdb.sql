create database bugless DEFAULT CHARACTER SET utf8;
create USER qaer@localhost IDENTIFIED BY 'qaer';
grant all on bugless.* to 'qaer';
flush privileges;
