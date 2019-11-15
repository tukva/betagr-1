create database test_db;
create user admin;
alter user admin superuser createrole createdb;
alter database test_db owner to admin;
ALTER USER admin WITH ENCRYPTED PASSWORD 'admin';