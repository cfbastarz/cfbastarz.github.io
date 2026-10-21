---
title: 'Comando não encontrado: add-apt-repository (Ubuntu 12.10)'
date: '2013-03-10 15:55:15'
tags:
- Tudo
- Tutoriais
- Ubuntu Server 12.10
- add-apt-repository
categories:
- Tudo
- Tutoriais
wordpress_id: 1995
original_url: https://craftmind.wordpress.com/2013/03/10/comando-nao-encontrado-add-apt-repository-ubuntu-12-10/
---

# Comando não encontrado: add-apt-repository (Ubuntu 12.10)

Esta é rápida:

Estava utilizando o Ubuntu Server 12.10 e queria adicionar um repositório novo utilizando o comando "sudo add-apt-repository", quando obtive o seguinte erro:


```
“add-apt-repository” command not found
```


Para resolver, instalei os seguintes pacotes:

- python-software-properties
- software-properties-common

Para instalar, basta fazer:


```
$ sudo apt-get install python-software-properties software-properties-common
```


É isso!

**Referência:**

<http://blog.xrmplatform.org/solution-for-add-apt-repository-command-not-found-ubuntu-12-10-server/>
