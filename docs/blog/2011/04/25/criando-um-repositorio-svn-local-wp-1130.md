---
title: Criando um repositório SVN local
date: '2011-04-25 17:27:04'
tags:
- SVN
- Subversion
- Tudo
- Tutoriais
- repositório local SVN
categories:
- Tudo
- Tutoriais
wordpress_id: 1130
original_url: https://craftmind.wordpress.com/2011/04/25/criando-um-repositorio-svn-local/
---

# Criando um repositório SVN local

Para criar um repositório SVN é fácil. Basta escolher um local da máquina e rodar o seguinte comando:


```
$ svnadmin create nome_do_repositorio
```


Com isso, é criada uma pasta de nome “nome_do_repositorio” que é o repositório propriamente dito. Para utilizá-lo, tem que configurar dois arquivos: o svnserve.conf e o passwd. Ambos os arquivos estão dentro da pasta conf, dentro do repositório. No svnserve.conf, temos que configurar as permissões de leitura/escrita, o arquivo que conterá as senhas de acesso e o nome do repsoitório (realm), como se segue:


```
[general]
 ### These options control access to the repository for unauthenticated
 ### and authenticated users.  Valid values are "write", "read",
 ### and "none".  The sample settings below are the defaults.
 anon-access = read
 auth-access = write
### If SASL is enabled (see below), this file will NOT be used.
 ### Uncomment the line below to use the default password file.
 password-db = passwd
### This option specifies the authentication realm of the repository.
 ### If two repositories have the same authentication realm, they should
 ### have the same password database, and vice versa.  The default realm
 ### is repository's uuid.
 realm = Repositório local
```


No arquivo passwd.conf, adicionamos os usuários que terão acesso ao repositório, como abaixo:


```
carlos = carlos.
```


Para ativar o repositório basta rodar o seguinte comando:


```
$ svnserve -d -r /pasta/onde/esta/o/repositorio
```


No comando svnserve, o modificador “-d” é para daemon e “-r” é para indicar onde está o repositírio. Fácil não?
