---
title: Sincronizando o Macports através do HTTP
date: '2013-09-10 15:13:56'
tags:
- Internet
- MacPorts
- Tudo
- Tutoriais
- http
- rsync
categories:
- Internet
- Tudo
- Tutoriais
wordpress_id: 2147
original_url: https://craftmind.wordpress.com/2013/09/10/sincronizando-o-macports-atraves-do-http/
---

# Sincronizando o Macports através do HTTP

O Macports é uma espécie de apt-get do (Mac) OS X: com ele é possível instalar praticamente todo o software de linha de comando (e alguns gráficos também) que você precisa. Eu uso muito ela para instalar software como wget, ncft, grads, ncl, cdo, nco, core-utils, grep, sed, awk etc. Clique [aqui](http://craftmind.wordpress.com/?s=macports&submit=Pesquisa) para encontrar todos os post relacionado ao Macports.

Por default, o Macports utiliza o rsync para fazer a atualização dos pacotes disponíveis, mas dependendo da rede em que o seu Mac está conectado, não é possível utilizar o rsync e, consequentemente, não é possível atualizar a lista de pacotes disponíveis:


```
$ sudo port selfupdate
Password:
--->  Updating MacPorts base sources using rsync
Error: Error synchronizing MacPorts sources: command execution failed
Please run `port -v selfupdate' for details.
Error: /opt/local/bin/port: port selfupdate failed: Error synchronizing MacPorts sources: command execution failed
```


No entanto, é possível fazer a sincronização dos pacotes através do protocolo HTTP. Para isto, basta fazer (considerando que o seu Macports está instalado em /opt/local):

**1) Modificar o arquivo /opt/local/etc/macports/sources.conf a adicionar a linha abaixo:**


```
https://distfiles.macports.org/ports.tar.gz [default]
```


O arquivo deve ficar assim:


```
#rsync://rsync.macports.org/release/tarballs/ports.tar [default]
https://distfiles.macports.org/ports.tar.gz [default]
```


**2) Atualizar a lista de pacotes do Macports com o comando:**


```
$ sudo port -d sync
```


Pronto, Macports funcionando novamente!

**Referência:**

- <http://trac.macports.org/wiki/howto/PortTreeTarball>
