---
title: Utilizando o SSH sem senha no linux
date: '2011-02-25 17:20:29'
tags:
- Internet
- SSH sem senha
- Tudo
- Tutoriais
- openssh-server
categories:
- Internet
- Tudo
- Tutoriais
wordpress_id: 1122
original_url: https://craftmind.wordpress.com/2011/02/25/utilizando-o-ssh-sem-senha-no-linux/
---

# Utilizando o SSH sem senha no linux

O SSH ou “Secure SHell” é um programa cliente/servidor (no sentido de que pode-se executar apenas o cliente – o básico, ou o servidor – o completo) que permite o usuário fazer conexões remotas utilizando o shell do linux de forma segura. Um recurso bastante interessante do SSH é que ele pode ser executado sem senha, o que facilita bastante a vida de quem precisa desse recurso, como por exemplo, em ambientes de execução de códigos paralelizados, em que são necessárias conexões seguras entre os nós de processamento, que são feitas via SSH. Então, para habilitar este recurso (ssh sem senha), basta seguir os passos abaixo (considerando a utilização do Ubuntu ou algum derivado do Debian):

Instalar o servidor do SSH


```
$ sudo apt-get install openssh-server
```


Criar uma chave pública do SSH


```
$ ssh-keygen -t rsa
```


* Neste passo, pode-se aceitar tanto a passphrase em branco quanto o local de armazenamento da chave, geralmente em $HOME/.ssh

Adicionar o conteúdo da chave para o arquivo que será lido pelo servidor (authorized_keys)


```
$ cd $HOME/.ssh
$ cat id_rsa.pub >> authorized_keys
```


Teste do ssh na máquina local (localhost)


```
$ ssh localhost whoami
```


Os provedimentos acima funcionam apenas para a máquina local. Caso queira-se fazer com que o acesso à um servidor ou máquina remota funcione da mesma forma, basta copiar a chave pública id_rsa.pub para o servidor (ou máquina local) e adicionar o seu conteúdo ao arquivo authorized_keys da máquina remota.

Copiando o arquivo id_rsa.pub para a máquina remota utilizando o comando SCP:


```
$ cd $HOME/.ssh
$ scp id_rsa.pub usuario@servidor/.ssh/id_rsa.pub.localhost
$ ssh usuario@servidor
$ cd $HOME/.ssh
$ cat id_rsa.pub.localhost >> authorized_keys
```


Vale lembrar que a instalação do openssh-server é crucial para o funcionamento do SSH sem senha na máquina local, apenas.
