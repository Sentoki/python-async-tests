create database async_database_tests;
create table names
(
    id   serial primary key,
    name varchar
);

INSERT INTO names (id, name)
VALUES (1, 'john'),
       (2, 'jake');
