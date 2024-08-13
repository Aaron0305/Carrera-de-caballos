create table usuario(
userId integer Primary Key,
nombre varchar2(20),
relEmpresaID integer);

create table empresa(
empresaId integer primary key,
empresa varchar2(20),
dirEmpresa varchar2(30));

create table url(
urlId integer primary key,
urlDescr varchar2(20));

create table urlRelacion(
relacionID integer primary key,
relacionUrlId integer,
relacionUserId integer);


