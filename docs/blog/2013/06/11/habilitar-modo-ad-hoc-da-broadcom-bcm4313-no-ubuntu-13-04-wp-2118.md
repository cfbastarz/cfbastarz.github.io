---
title: Habilitar modo Ad-Hoc da Broadcom BCM4313 no Ubuntu 13.04
date: '2013-06-11 23:33:51'
tags:
- Tudo
- Tutoriais
- ad-hoc
- bcm4313
- ubuntu 13.04
categories:
- Tudo
- Tutoriais
wordpress_id: 2118
original_url: https://craftmind.wordpress.com/2013/06/11/habilitar-modo-ad-hoc-da-broadcom-bcm4313-no-ubuntu-13-04/
---

# Habilitar modo Ad-Hoc da Broadcom BCM4313 no Ubuntu 13.04

Para habilitar o modo ad-hoc (para fazer uma rede ponto-a-ponto) da placa wireless Broadcom bcm4313, descobri que era necessário instalar um pacote extra no Ubuntu 13.04.

Para identificar a placa:



```
$ lspci | grep -i broadcom
```




```
02:00.0 Network controller: Broadcom Corporation BCM4313 802.11b/g/n Wireless LAN Controller (rev 01)
```



E para atualizar e instalar o pacote faltante:



```
$ sudo apt-get update
```




```
$ sudo apt-get install bcmwl-kernel-source
```



E pronto!
