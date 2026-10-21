---
title: Recuperando o carregamento do Windows no GRUB
date: '2011-09-06 11:01:08'
tags:
- Dual-boot
- GRUB
- Tudo
- Tutoriais
- os-prober
- update-grub
categories:
- Tudo
- Tutoriais
wordpress_id: 1255
original_url: https://craftmind.wordpress.com/2011/09/06/recuperando-o-carregamento-do-windows-no-grub/
---

# Recuperando o carregamento do Windows no GRUB

Esses dias fui atualizar uma instalação Ubuntu 9.04 em dual-boot (linux + windows, no mesmo HD) e ao reiniciar, acabei perdendo a entrada do Windows no GRUB. O que fazer? Pesquisando por uma solução rápida, descobri o programa os-prober, que procura por sistemas que tenham algum tipo de "loader" e os adiciona ao sistema de carregamentodo linux, no meu caso o GRUB.

Para instalar o os-prober, e readicionar o a linha de comando que carrega o windows, faça o seguinte:


```
$ sudo apt-get install os-prober && sudo os-prober && sudo update-grub
```


Referências:

- <http://kitenet.net/~joey/code/os-prober/>
- <http://spiralofhope.com/lubuntu.html>
