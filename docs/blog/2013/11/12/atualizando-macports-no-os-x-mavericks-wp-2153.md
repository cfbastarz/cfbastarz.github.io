---
title: Atualizando Macports no OS X Mavericks
date: '2013-11-12 22:43:27'
tags:
- MacPorts
- OS X Mavericks
- Tudo
- Tutoriais
categories:
- Tudo
- Tutoriais
wordpress_id: 2153
original_url: https://craftmind.wordpress.com/2013/11/12/atualizando-macports-no-os-x-mavericks/
---

# Atualizando Macports no OS X Mavericks

Se você atualizou o seu OS X Mountain Lion (e possivelmente o Snow Leopard e o Lion) para o Mavericks e não conseguiu atualizar o Macports, siga as instruções abaixo.

Depois de realizar o upgrade do OS X Mountain Lion para o Mavericks, o Macports apresentou o seguinte erro (para o qual, a solução segue mais adiante):


```
Command failed: cd /opt/local/var/macports/sources/rsync.macports.org/release/tarballs/base && CC=/usr/bin/cc OBJC=/usr/bin/cc ./configure --prefix=/opt/local --with-tclpackage=/Library/Tcl --with-install-user=root --with-install-group=admin --with-directory-mode=0755 --enable-readline && make SELFUPDATING=1 && make install SELFUPDATING=1
Exit code: 1
Error: Error installing new MacPorts base: command execution failed
To report a bug, follow the instructions in the guide:
 http://guide.macports.org/#project.tickets
Error: /opt/local/bin/port: port selfupdate failed: Error installing new MacPorts base: command execution failed
```


**1) Instale o "Command Line Tools"**


```
$ sudo xcode-select --install
```


**2) Aceite a licença do XCode**


```
$ sudo xcodebuild -license
```


**3) Atualize o Macports**


```
$ sudo port -v selfupdate
```


**Referência:**

- <http://stackoverflow.com/questions/19622337/cant-update-macports-with-mac-os-x-mavericks>
