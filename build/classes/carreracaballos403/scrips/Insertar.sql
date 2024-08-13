delete from urlRelacion;
delete from usuario;
delete from empresa;
delete from url;

insert all
into empresa (empresaId, empresa, dirEmpresa) values (1,'ABC','1 Work Lane')
into empresa (empresaId, empresa, dirEmpresa) values (2,'Jil','1 Job Street')
select *from dual;
insert all
into url (urlId, urlDescr) values (1,'abc.com')
into url (urlId, urlDescr) values (2,'xyz.com')
select *from dual;

insert all
into usuario (userId, nombre,relEmpresaId) values (1,'Joe',1)
into usuario (userId, nombre,relEmpresaId) values (2,'Jil',2)
select *from dual;



insert all
into urlRelacion (relacionID, relacionUrlId,relacionUserId) values (1,1,1)
into urlRelacion (relacionID, relacionUrlId,relacionUserId) values (2,1,2)
into urlRelacion (relacionID, relacionUrlId,relacionUserId) values (3,2,1)
into urlRelacion (relacionID, relacionUrlId,relacionUserId) values (4,2,2)
select *from dual;

