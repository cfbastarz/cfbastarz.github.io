---
title: Zero Fill
date: '2011-12-17 16:57:42'
tags:
- Tudo
- Tutoriais
- shred
- zero fill
categories:
- Tudo
- Tutoriais
wordpress_id: 1361
original_url: https://craftmind.wordpress.com/2011/12/17/zero-fill/
---

# Zero Fill

No linux há um comando bastante útil e que permite "realmente" apagar o conteúdo de uma disco rígido inteiro ou partição. Esse processo de apagar um conteúdo de forma mais segura, é também cinhecido como Zero Fill e é um conceito global da informática, não sendo restrito a uma plataforma (como o linux) ou outra. No linux, o nome desse comando shred, e uma exemplo de sua aplicação é a seguinte:


```
$ sudo shred -n 2 -z -v /dev/sda1
```


Nesse comando, as opções fazem o seguinte:

- -n 2: é a quantidade de vezes que a partição será preenchida com zeros (quanto mais, melhor - e muito mais demorado);
- -z: indica que os seus dados serão sobrescritos com zeros;
- -v: modo verbose.

Com esse comando, a partição "/dev/sda1" será sobrescrita 2 vezes com zeros. Isso é suficiente para que dados antigos seja "definitivamente" eliminados do HD.
