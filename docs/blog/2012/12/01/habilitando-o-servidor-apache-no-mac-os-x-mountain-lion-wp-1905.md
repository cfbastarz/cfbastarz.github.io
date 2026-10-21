---
title: Habilitando o servidor Apache no Mac OS X Mountain Lion
date: '2012-12-01 10:33:59'
tags:
- Apache
- Internet
- Mac OS X
- Mountain Lion
- Tudo
- Tutoriais
categories:
- Internet
- Tudo
- Tutoriais
wordpress_id: 1905
original_url: https://craftmind.wordpress.com/2012/12/01/habilitando-o-servidor-apache-no-mac-os-x-mountain-lion/
---

# Habilitando o servidor Apache no Mac OS X Mountain Lion

Ter um servidor Apache instalado na sua máquina, seja um notebook ou desktop, é uma mão na roda quando se precisa testar um website, permitindo até que outros computadores na rede possam acessá-lo, ajudando-o a testar o site em diferentes navegadores, em diferentes sistemas operacionais (acredite, o Firefox, o Opera  e o Chrome do windows, podem rendererizar diferentemente no linux).

Quando eu comprei o meu MacBook Pro, logo descobri como habilitar o Apache com PHP, e isso foi muito fácil, tal como descrevi [aqui](../../05/17/habilitando-o-servidor-apache-com-php-no-mac-os-x-lion-wp-1558.md).

Mas depois que atualizei para o Mac OS X Mountain Lion, não percebi um detalhe: a opção para habilitar o "Web Sharing" (ou Compartilhamento Web) no painel de controle do Mac OS X, sumiu! Procurando na internet, encontrei este [link](http://reviews.cnet.com/8301-13727_7-57481978-263/how-to-enable-web-sharing-in-os-x-mountain-lion/) que ensina a habilitar o servidor Apache do Mac OS X Mountain Lion, mesmo sem ter a opção no painel de controle. Se você está acostumado com o Linux, vai perceber que os procedimentos são muito parecidos - para não dizer praticamente os mesmos. Para facilitar um pouco as coisas, vou resumir os comandos aqui.

**Procedimentos**

O primeiro passo, é entrar na pasta "/etc/apache2/users/" e criar um arquivo de configuração com o seu nome de usuário:


```
$ cd /etc/apache2/users/
$ sudo touch `whoami`.conf
```


A seguir, inclua as seguintes linhas nesse arquivo:


```
<Directory "/Users/usuario/Sites/">
     Options Indexes MultiViews
     AllowOverride All
     Order allow,deny
     Allow from all
</Directory>
```


Observe que a palavra "usuario" deve ser substituída pelo seu nome de usuário, que pode ser obtido a partir do comando "whoami" :)

Depois, basta iniciar o Apache com o seguinte comando:


```
$ sudo apachectl start
```


Dessa forma, o Apache será desabilitado quando você desligar o computador. Caso queira encerrar o Apache antes, basta executar o seguinte comando:


```
$ sudo apachectl stop
```


Para terminar a configuração, ajuste as permissões de acesso ao Apache com os seguintes comandos:


```
$ sudo chown root:wheel /etc/apache2/users/*
$ sudo chmod 644 /etc/apache2/users/*
```


Para acessar os sites que você estiver editando/testando, basta colocá-los na pasta "Sites" no seu home (se ela não existir, basta criá-la) e digitar o seguinte endereço no seu navegador:


```
http://localhost/~usuario
```


Lembrando que "usuario" é o seu nome de usuário. Para que outros computadores da rede possam acessar o seu computador a partir do navegador, basta fornecer o endereço de IP ou o nome da máquina. Exemplos, "http://nome.da.maquina/~usuario" ou "http://123.456.789/~usuario".

**Dicas**

Se você quiser deixar o Apache ativo o tempo todo, mesmo depois de reiniciar o computador, basta executar o comando:


```
$ sudo defaults write /System/Library/LaunchDaemons/org.apache.httpd Disabled -bool false
```


... e se quiser desfazer esse comando (ou seja, fazer com que o Apache não inicie sozinho depois de ligar o computador), basta fazer:


```
$ sudo defaults write /System/Library/LaunchDaemons/org.apache.httpd Disabled -bool true
```


Referência

- <http://reviews.cnet.com/8301-13727_7-57481978-263/how-to-enable-web-sharing-in-os-x-mountain-lion/>
