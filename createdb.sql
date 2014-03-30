create database qa_platform;
create USER qaer@localhost IDENTIFIED BY 'qaer';
grant all on qa_platform.* to 'qaer';
flush privileges;
