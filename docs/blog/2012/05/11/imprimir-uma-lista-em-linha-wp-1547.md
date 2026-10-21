---
title: Imprimir uma lista em linha
date: '2012-05-11 14:26:40'
tags:
- Tudo
- Tutoriais
- sed
- seq
categories:
- Tudo
- Tutoriais
wordpress_id: 1547
original_url: https://craftmind.wordpress.com/2012/05/11/imprimir-uma-lista-em-linha/
---

# Imprimir uma lista em linha

Nota mental:

Com o comando seq, podemos listar uma sequência entre dois números inteiros quaisquer:


```
$ seq 5
1
2
3
4
5
```


Mas como fazer para imprimir na horizontal (em linha): "1 2 3 4 5"?

Com o sed, dá:


```
$ seq 5 | sed -e :a -e "{N; s,\n, ,g; ta}"
1 2 3 4 5
```


Fim!
