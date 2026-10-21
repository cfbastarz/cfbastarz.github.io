---
title: Instalando manualmente o JRE no Ubuntu 12.04
date: '2012-04-05 02:23:14'
tags:
- JAVA
- Tudo
- Tutoriais
- java plugin firefox
- jre
- ubuntu 12.04
- ubuntu precise
categories:
- Tudo
- Tutoriais
wordpress_id: 1484
original_url: https://craftmind.wordpress.com/2012/04/05/instalando-manualmente-o-jre-no-ubuntu-12-04/
---

# Instalando manualmente o JRE no Ubuntu 12.04

No momento em que escrevo este post, o Ubuntu 12.04 (Precise Pangolin) está na reta final de desenvolvimentos, com o seu último beta lançado antes do anúncio final. Mas há algum tempo, vários sites na internet já disponibilizam ppas para a instalação de programas e que facilitam bastante a vida de quem precisa de um pacote mais atualizado ou de algum programa que não existe nos respositórios oficiais. Com a mudança de licença da Oracle, há pelo menos uma versão, o Ubuntu deixou de distribuir o pacote de desenvolvimento java da Oracle e passou a oferecer a sua versão open-source. Como no caso da versão open source do flash-player, algumas aplicações não funcionam corretamente e sempre temos quue recorrer ao mal necessário das versões originais.

Para a instalação do pacote de desenvolvimento Java (incluindo o plugin para o Firefox), há um ou dois ppas disponíveis que não estão funcionando corretamente (pelo menos falhou em minhas tentativas). Por isso, resolvi buscar a solução mais "slackware" e resolver o meu problema. Se esse for também o seu caso, siga o passo a passo:
1) Instale o pacote alien no seu Ubuntu 12.04


```
$ sudo apt-get install alien
```


2) Baixe o pacote jre-7u3-linux-x64.rpm no site da Oracle
3) Transforme o baixado de rpm para deb


```
$ sudo alien --scripts jre-7u3-linux-x64.rpm
```


4) Instale o pacote gerado


```
$ sudo dpkg -i jre_1.7.003-1_amd64.deb
```


Até aqui tudo o que fizemos foi instalar o pacote de desenvolvimento Java no Ubuntu 12.04. A instalação pode ser verificada como o resultado do comando "$ whereis java". Como este é um método alternativo, temos que instalar o plugin java para o Firefox. Para isso, execute os seguintes comandos:
5) Entre na pasta de plugins do firefox


```
$ cd /usr/lib/firefox/plugins
```


6) Crie um link simbólico para o plugin do java


```
$ sudo ln -s /usr/java/jre1.7.0_03/lib/amd64/libnpjp2.so .
```


Não se esqueça do ponto ao final. É isso!
