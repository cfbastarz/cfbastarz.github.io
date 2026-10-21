---
title: Instalando a biblioteca JPEG no linux
date: '2011-01-25 17:16:14'
tags:
- JPEG
- Tudo
- Tutoriais
- libjpeg
categories:
- Tudo
- Tutoriais
wordpress_id: 1118
original_url: https://craftmind.wordpress.com/2011/01/25/instalando-a-biblioteca-jpeg-no-linux/
---

# Instalando a biblioteca JPEG no linux

Para instalar a biblioteca JPEG a partir do código-fonte é bastante fácil, mas para o usuário menos experiente, há que se considerar alguns detalhes:

Antes de se executar o comando de instalação “make install-lib”, há que se criar manualmente os diretórios “include” e “lib”. Em sequência, os comandos para baixar, configurar e instalar o pacote são:


```
$ wget -c http://www.hdfgroup.org/ftp/lib-external/jpeg/src/jpegsrc.v6b.tar.gz
$ tar -zxvf jpegsrc.v6b.tar.gz
$ cd jpegsrc.v6b
$ ./configure --prefix=/opt/jpegsrc.v6b
$ make
$ sudo mkdir /opt/jpegsrc.v6b/lib /opt/jpegsrc.v6b/include
$ sudo make install-lib
```


Prontinho!
